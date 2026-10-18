from request.user import UserRequest
from model.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from security import hash

async def create_user(db: AsyncSession, user_data: UserRequest):
    result = await db.execute(select(User).where(User.name == user_data.name))
    if result.scalar():
        return False

    hash_pwd = await hash.get_hash(user_data.password)
    user = User(name=user_data.name, password=hash_pwd)
    db.add(user)          # add 是同步方法，不需要 await
    await db.commit()
    await db.refresh(user)
    return user


async def login_user(db: AsyncSession, user_data: UserRequest):
    result = await db.execute(select(User).where(User.name == user_data.name))
    user = result.scalar()
    if not user:
        return False

    is_valid = await hash.verify(user_data.password, user.password)
    if not is_valid:
        return False
    return user