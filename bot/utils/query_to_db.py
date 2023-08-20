from database.models import Bank, User
from database.connect import create_session
from utils.parser import Parser
from utils.serializers import Serialiser

from datetime import datetime

from utils.my_logger import log
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


async def _write_currency_data_in_db():
    """
    Write parse-data in DB
    Used at the beggining of the bot start to populate the DB
    """
    parser = Parser()
    async with create_session() as session:
        for data in parser.parse_html():
            name, surrender, buy = data
            bank = Bank(name=name, 
                        buy_currency=buy, 
                        surrender_currency=surrender,
                        update_time=datetime.now())
            
            session: AsyncSession
            session.add(bank)

async def get_banks_data_in_db() -> str:
    """
    Return all info about banks from DB to str format
    """
    query = select(Bank)
    async with create_session() as session:
        session: AsyncSession
        result = await session.execute(query)
        data = result.scalars().all()

    serializer = Serialiser(data)
    return serializer.to_text()

async def add_user_in_db(data: dict):
    """
    Add new user in DB
    """
    tg_id=data.get("tg_id")
    username = data.get("username", None)

    user = User(tg_id=tg_id,
                username=username)            
    
    async with create_session() as session:
        if await user_is_exists_in_db(session, tg_id):
            return
        
        session: AsyncSession
        session.add(user)
    log.critical(f"Create new user with username - {username}")

async def user_is_exists_in_db(session: AsyncSession, tg_id: str) -> bool:
    user_in_db = await session.execute(select(User).where(User.tg_id == tg_id))
    is_exists = user_in_db.scalars().first()
    if is_exists:
        return True
    return False



async def update_banks_in_db():
    """
    Update data the banks in DB
    Used oce on a day to update data
    """
    parser = Parser()

    async with create_session() as session:
        session: AsyncSession

        for data in parser.parse_html():
            name, surrender, buy = data
            params = {
                "name": name,
                "buy_currency": buy,
                "surrender_currency": surrender,
            }
            query = update(Bank).where(Bank.name == name).values(**params).execution_options(synchronize_session='fetch')
            await session.execute(query)
    log.critical("Processe update banks info complite")
        

