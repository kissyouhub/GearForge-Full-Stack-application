from typing import AsyncGenerator

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session
from app.config import get_settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings





engine = create_async_engine(settings.database_url, pool_pre_ping = True)

Sessionlocal = async_sessionmaker[AsyncSession](bind=engine, expire_on_commit=False, autoflush=False)

async def get_db() -> AsyncGenerator[AsyncSession, None ]:
    async with Sessionlocal() as db:
        yield db