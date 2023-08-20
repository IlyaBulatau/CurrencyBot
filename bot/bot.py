from aiogram import Bot, Dispatcher

import asyncio

from handlers.handlers import router as handlers_router
from handlers.commands import router as commands_router
from settings.settings import BotSettings
from utils.menu import setup_menu
from database.db import Database
from utils.query_to_db import _write_currency_data_in_db


async def create_bot():
    """
    Create bot and run startup processes
    """
    settings = BotSettings()

    bot = Bot(settings.token)
    ds = Dispatcher()

    await bot(setup_menu()) # setup menu

    ds.include_routers( # setup routers
        commands_router,
        handlers_router
    )

    await Database().create_database() # create database if not exists
    # await _write_currency_data_in_db() # write data or rollback

    await ds.start_polling(bot) # run bot

if __name__ == "__main__":
    asyncio.run(create_bot())

# TODO - add logging
# TODO - add celery