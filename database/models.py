from sqlalchemy import BigInteger
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs

from config import sqlalchemy_url

engine = create_async_engine(sqlalchemy_url, echo=True)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column((BigInteger()))
    username: Mapped[str] = mapped_column(String(30))


class Reviews(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column((String(250)))
    caption: Mapped[str] = mapped_column(String(50))


async def async_main():
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.create_all)
        except Exception as e:
            print('error', e)

