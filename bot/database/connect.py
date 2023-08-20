from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from contextlib import asynccontextmanager

from settings.settings import DatabaseSettings


engine = create_async_engine(url=DatabaseSettings().url, echo=True, future=True) 
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)


@asynccontextmanager
async def create_session() -> AsyncSession:
    session = session_factory()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
    finally:
        await session.close()