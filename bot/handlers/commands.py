from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    # add middleware register user in DB
    await message.answer(text="Register in DB")