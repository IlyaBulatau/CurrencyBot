"""
Logging Module
file log - DEBUG Level
stream log - WARNING Level
email log - CRITICAL Level
"""
import logging
from logging.handlers import SMTPHandler
import pathlib

from settings.settings import BotSettings


settings = BotSettings()
FILE_NAME = "log.log"
PATH_TO_FILE = pathlib.Path().absolute().joinpath("bot").joinpath("utils").joinpath(FILE_NAME)

log = logging.getLogger(__name__)
log.setLevel("DEBUG")

formatter = logging.Formatter(fmt="{asctime} {levelname} {message}", style="{")

file_handlers = logging.FileHandler(filename=PATH_TO_FILE, mode="a", encoding="utf-8")
file_handlers.setLevel("DEBUG")
file_handlers.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel("WARNING")
stream_handler.setFormatter(formatter)

email_handler = SMTPHandler(
    mailhost=('smtp.yandex.ru', 587),
    fromaddr=settings.email,
    toaddrs=settings.email,
    subject="Currency Bot",
    credentials=(settings.email, settings.email_password),
    secure=(),
)
email_handler.setLevel("CRITICAL")
email_handler.setFormatter(formatter)

log.addHandler(file_handlers)
log.addHandler(stream_handler)
log.addHandler(email_handler)