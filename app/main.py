from fastapi import FastAPI
from app.routers import auth, order, portfolio, websocket
import asyncio
from app.services.price_feed import simulate_prices

app = FastAPI(title="Real-Time Stock Exchange API")

app.include_router(auth.router)
app.include_router(order.router)
app.include_router(portfolio.router)
app.include_router(websocket.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(simulate_prices())
