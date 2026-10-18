from fastapi import APIRouter,Depends
from config.db_conf import get_db
from request.user import UserRequest
from sqlalchemy.ext.asyncio import AsyncSession
from crud.user import create_user,login_user,create_token

router = APIRouter()

@router.post('/register')
async def register(user:UserRequest,db:AsyncSession=Depends(get_db)):
    user_data = await create_user(db,user)
    await create_token(db,user)
    return {"message":"注册成功",'data':user_data}

@router.post('/login')
async def login(user:UserRequest,db:AsyncSession=Depends(get_db)):
    user_data = await login_user(db,user)
    await create_token(db,user)
    return {"message":"登录成功",'data':user_data}