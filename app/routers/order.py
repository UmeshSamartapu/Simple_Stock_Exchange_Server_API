from fastapi import APIRouter, Depends, HTTPException
from app.models import Order
from datetime import datetime
from app.db import orders_collection, users_collection
from app.utils import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/")
async def place_order(order: Order, current_user=Depends(get_current_user)):
    if order.user_email != current_user["email"]:
        raise HTTPException(status_code=403, detail="Cannot place order for other users")

    order.timestamp = datetime.utcnow()
    await orders_collection.insert_one(order.dict())

    portfolio = current_user.get("portfolio", [])
    found = False
    for item in portfolio:
        if item["stock_symbol"] == order.stock_symbol:
            if order.order_type == "buy":
                item["quantity"] += order.quantity
            elif order.order_type == "sell":
                if item["quantity"] < order.quantity:
                    raise HTTPException(status_code=400, detail="Not enough stocks to sell")
                item["quantity"] -= order.quantity
            found = True
            break

    if not found and order.order_type == "buy":
        portfolio.append({"stock_symbol": order.stock_symbol, "quantity": order.quantity})

    portfolio = [item for item in portfolio if item["quantity"] > 0]

    await users_collection.update_one({"email": current_user["email"]}, {"$set": {"portfolio": portfolio}})

    return {"msg": "Order placed", "portfolio": portfolio}
