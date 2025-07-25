from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config.settings import Settings

Base = declarative_base()


class Database:
    def __init__(self):
        self.params = Settings()
        self.url = self.params.DATABASE_URL
        self.engine = create_async_engine(self.url, echo=True)
        self.async_session = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def get_session(self):
        return self.async_session()


db = Database()
