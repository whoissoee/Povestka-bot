import asyncio
import logging
import sys

from signature import dp, bot
from handlers.user import router
from handlers.admin import admin
from database.models import async_main


async def main():
    await async_main()

    dp.include_routers(router, admin)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')