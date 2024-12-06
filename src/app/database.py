from typing import AsyncGenerator
# from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.app.config import DB_NAME, DB_HOST, DB_PASS, DB_PORT, DB_USER

# Base: DeclarativeMeta = declarative_base()

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield {"session": session}

