FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /bot

RUN pip install poetry

COPY poetry.lock pyproject.toml /bot/

COPY . /bot

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi && poetry build

COPY .env /

COPY docker-entrypoint.sh /

RUN chmod 777 docker-entrypoint.sh  

ENTRYPOINT ["./docker-entrypoint.sh"]
