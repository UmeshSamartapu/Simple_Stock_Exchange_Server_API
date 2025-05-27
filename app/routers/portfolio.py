from fastapi import APIRouter, Depends
from app.utils import get_current_user

router = APIRouter(prefix="/portfolio", tags=["portfolio"])

@router.get("/")
async def get_portfolio(current_user=Depends(get_current_user)):
    return {"portfolio": current_user.get("portfolio", [])}
