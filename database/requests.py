from sqlalchemy import select, insert, and_, delete
from database.models import async_session, User, Reviews


class UserDb:
    @staticmethod
    async def check_user(user_id):
        async with async_session() as session:
            query = select(User).where(User.user_id == user_id)
            result = await session.execute(query)
            user = result.scalar()
            if user is not None:
                return True
            else:
                return False
    
    @staticmethod
    async def add_user(user_id, username):
        async with async_session() as session:
            await session.execute(insert(User).values(user_id=user_id, username=username))
            await session.commit()

    @staticmethod
    async def add_reviews(photo, caption):
        async with async_session() as session:
            await session.execute(insert(Reviews).values(photo=photo, caption=caption))
            await session.commit()

    @staticmethod
    async def get_reviews():
        async with async_session() as session:
            query = select(Reviews.photo, Reviews.caption)
            result = await session.execute(query)
            reviews = result.fetchall()
            return reviews
