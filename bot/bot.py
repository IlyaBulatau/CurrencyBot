from aiogram import Bot, Dispatcher

import asyncio

from handlers.handlers import router as handlers_router
from handlers.commands import router as commands_router
from settings.settings import Settings
from utils.menu import setup_menu


async def create_bot():
    settings = Settings()

    bot = Bot(settings.token)
    ds = Dispatcher()

    await bot(setup_menu())

    ds.include_routers(
        handlers_router,
        commands_router
    )

    # ds.startup.register()
    # ds.shutdown.register()

    await ds.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(create_bot())

# TODO - connect postgres
