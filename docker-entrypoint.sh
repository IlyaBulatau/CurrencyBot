#!/bin/sh

alembic upgrade head

python ./bot/bot.py