import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.config.settings import Settings
from src.infra.database.db import Base

# Alembic Config object
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata das models
target_metadata = Base.metadata


# Função que pega a URL do banco de dados via settings
def get_database_url():
    return Settings().DATABASE_URL


# Offline migrations (gera SQL sem conectar ao banco)
def run_migrations_offline() -> None:
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# Função auxiliar para rodar as migrations online
def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


# Online migrations com suporte a async
async def run_migrations_online() -> None:
    connectable: AsyncEngine = create_async_engine(
        get_database_url(),
        poolclass=None,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


# Seleciona o modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
