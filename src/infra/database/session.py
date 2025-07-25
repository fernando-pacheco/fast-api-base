from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.db import db


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.async_session() as session:
        yield session
