# Telegram currency tracking bot

## How run?
First of all, clone the repository, rename the file `.env.example` to`.env` and set the environment variables to your data.

## Run in Docker
1. `make up` - build and run docker containers
2. `make logs` - container log entries
3. `make stop` - stop and remove all containers
4. `make psql` - enter db container with you login

##### If you run in Docker, your DB_HOST variables must be = your database container name, (default - db)!

## Run without Docker
1. Activate virtualenv.
```
poetry shell
```
2. Activate your environment variables.
```
export $(grep -v '^#' .env | xargs)
```
4. Run migrations.
```
alembic upgrade head
```
4. Run Bot.
```
python bot/bot.py
```
##### If you run without Docker, your DB_HOST variables must be = localhost!
