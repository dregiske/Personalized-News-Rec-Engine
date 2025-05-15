import os
import asyncio

import pytest_asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database import get_db, Base
from app.main     import app

TEST_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///:memory:")

@pytest_asyncio.fixture(scope="session")
async def async_engine():
    engine = create_async_engine(TEST_DATABASE_URL, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest_asyncio.fixture()
async def db_session(async_engine):
    async_session = sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session

@pytest.fixture(autouse=True)
def override_get_db(db_session):
    async def _get_db():
        yield db_session
    app.dependency_overrides[get_db] = _get_db

@pytest_asyncio.fixture
async def client_override():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client