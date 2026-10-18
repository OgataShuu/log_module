from passlib import context

pwd_context = context.CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_hash(password:str):
    return pwd_context.hash(password)

async def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)