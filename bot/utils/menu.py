from aiogram.methods import SetMyCommands
from aiogram.types import BotCommand

def setup_menu():
    commands = SetMyCommands(commands=[
        BotCommand(
        command="start",
        description="Start over"
        ),
        BotCommand(
        command="currency",
        description="Currency exchange rate"
        )
    ])

    return commands

