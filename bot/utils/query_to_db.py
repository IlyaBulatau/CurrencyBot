from database.models import Bank, User
from database.connect import create_session
from utils.parser import Parser
from utils.serializers import Serialiser

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def _write_currency_data_in_db():
    parser = Parser()
    for data in parser.parse_html():
        name, surrender, buy = data

        bank = Bank(name=name, 
                    buy_currency=buy, 
                    surrender_currency=surrender,
                    update_time=datetime.now())
        
        async with create_session() as session:
            session: AsyncSession
            session.add(bank)

async def get_banks_data_in_db():
    
    query = select(Bank)
    async with create_session() as session:
        session: AsyncSession
        result = await session.execute(query)
        data = result.scalars().all()

    serializer = Serialiser(data)
    return serializer.to_text()

