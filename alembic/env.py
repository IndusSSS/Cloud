from logging.config import fileConfig
import os
import sys
from pathlib import Path
from sqlalchemy import create_engine, pool
from sqlmodel import SQLModel
from alembic import context

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import app.db  # noqa: F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

DATABASE_URL = os.getenv("POSTGRES_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL or "")


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=SQLModel.metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"), poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=SQLModel.metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
