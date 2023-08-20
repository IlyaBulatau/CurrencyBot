from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode

from utils.query_to_db import get_banks_data_in_db


router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    # add middleware register user in DB
    await message.answer(text="Hello")

@router.message(Command(commands=["currency"]))
async def currency_command(message: Message):
    text = await get_banks_data_in_db()
    await message.answer(text=text, parse_mode=ParseMode.HTML)