import asyncio

from src.infra.database.db import db


async def init_models():
    async with db.engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_models())
