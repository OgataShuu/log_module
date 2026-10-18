import uuid

from request.user import UserRequest
from model.user import User,User_token
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from security import hash

async def create_user(db: AsyncSession, user_request: UserRequest):
    result = await db.execute(select(User).where(User.name == user_request.name))
    if result.scalar():
        return False

    hash_pwd = await hash.get_hash(user_request.password)
    user = User(name=user_request.name, password=hash_pwd)
    db.add(user)          # add 是同步方法，不需要 await
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_name(db: AsyncSession, user_data: UserRequest):
    result = await db.execute(select(User).where(User.name == user_data.name))
    return result.scalar()

async def login_user(db: AsyncSession, user_request: UserRequest):
    result = await db.execute(select(User).where(User.name == user_request.name))
    user = result.scalar()
    if not user:
        return False

    is_valid = await hash.verify(user_request.password, user.password)
    if not is_valid:
        return False
    return user


async def create_token(db: AsyncSession, user_request: UserRequest):
    token = uuid.uuid4()
    user=await get_user_by_name(db, user_request)
    user_token = User_token(user_id=user.id, token=token)
    db.add(user_token)
    await db.commit()
    await db.refresh(user_token)
    return True