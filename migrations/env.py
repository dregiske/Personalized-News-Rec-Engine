import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

# 1) Load .env (must live at project root next to alembic.ini)
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# this is the Alembic Config object
config = context.config

# 2) Override the URL from alembic.ini with the real one from .env
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("DATABASE_URL not set in .env")
config.set_main_option("sqlalchemy.url", DB_URL)

# Interpret the config file for Python logging.
if config.config_file_name:
    fileConfig(config.config_file_name)

# 3) Import your app’s Base so Alembic can see your models
sys.path.insert(0, os.getcwd())           # ensure `app/` is on PYTHONPATH
from app.models import Base               # adjust if your models live elsewhere
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # Use create_engine on the real URL instead of engine_from_config
    connectable = create_engine(DB_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
