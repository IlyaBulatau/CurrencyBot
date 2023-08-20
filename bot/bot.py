from aiogram import Bot, Dispatcher

import asyncio

from handlers.handlers import router as handlers_router
from handlers.commands import router as commands_router
from settings.settings import BotSettings
from utils.menu import setup_menu
from database.db import Database


async def create_bot():
    """
    Create bot and run startup processes
    """
    settings = BotSettings()

    bot = Bot(settings.token)
    ds = Dispatcher()

    await bot(setup_menu()) # setup menu

    ds.include_routers( # setup routers
        handlers_router,
        commands_router
    )

    await Database().create_database() # create database

    await ds.start_polling(bot) # run bot

if __name__ == "__main__":
    asyncio.run(create_bot())

