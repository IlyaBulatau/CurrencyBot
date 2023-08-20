from sqlalchemy.engine import create_engine as ce
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from contextlib import asynccontextmanager

from bot.settings.settings import DatabaseSettings


engine = ce(url=DatabaseSettings().url, echo=True, future=True, _is_async=True) 
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)


@asynccontextmanager
async def session() -> AsyncSession:
    """
    Back session
    """
    new_session: AsyncSession = session_factory()
    try:
        yield new_session
        await new_session.commit()
    except:
        await new_session.rollback()
    finally:
        await new_session.close()

