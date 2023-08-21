#!/bin/sh

set -a
source .env
set +a

alembic upgrade head

python ./bot/bot.py