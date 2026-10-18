from sqlalchemy import Column, Integer, String,DateTime,ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True)
    create_time:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    name:Mapped[str] = mapped_column(String(255))
    password:Mapped[str] = mapped_column(String(255))


class User_token(Base):
    __tablename__ = "user_token"

    id:Mapped[int] = mapped_column(primary_key=True)
    create_time:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey("user.id"))
    token:Mapped[str] = mapped_column(String(255))