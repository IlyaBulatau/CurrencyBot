from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode

from utils.query_to_db import get_banks_data_in_db, add_user_in_db


router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    """
    Register new user in DB
    """
    tg_id = message.from_user.id
    username = message.from_user.username
    data = {
        "tg_id": tg_id,
        "username": username if username else None
    }
    await add_user_in_db(data)
    await message.answer(text=f"👋Hello {username if username else 'friend'}")

@router.message(Command(commands=["currency"]))
async def currency_command(message: Message):
    """
    Back to user currency
    """
    text = await get_banks_data_in_db()
    await message.answer(text=text, parse_mode=ParseMode.HTML)