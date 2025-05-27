from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.db import users_collection
from app.models import UserCreate
from app.utils import verify_password, get_password_hash, create_access_token, get_current_user
from pydantic import BaseModel
from typing import Any

router = APIRouter(prefix="/auth", tags=["auth"])

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/register", status_code=201)
async def register(user: UserCreate):
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = get_password_hash(user.password)
    user_doc = {"email": user.email, "hashed_password": hashed_pw, "portfolio": []}
    await users_collection.insert_one(user_doc)
    return {"msg": "User registered"}

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_collection.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def read_users_me(current_user: Any = Depends(get_current_user)):
    return {"email": current_user["email"], "portfolio": current_user.get("portfolio", [])}
