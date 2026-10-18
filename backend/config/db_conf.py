from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker

#url
URL='mysql+aiomysql://root:Shinzan202@localhost:3306/log'
#engine
engine = create_async_engine(
    url=URL
)
#sessionmaket
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession
)
#session
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()