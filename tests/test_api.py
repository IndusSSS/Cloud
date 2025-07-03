import os
os.environ.setdefault("POSTGRES_URL", "sqlite+aiosqlite:///:memory:")

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
import redis.asyncio as aioredis
import fakeredis.aioredis

from app.main import app
from app.db import init_db


@pytest_asyncio.fixture(autouse=True)
async def setup_db() -> None:
    await init_db()


@pytest_asyncio.fixture(autouse=True)
async def fake_redis(monkeypatch):
    fake = fakeredis.aioredis.FakeRedis()
    def _from_url(*args, **kwargs):
        return fake
    monkeypatch.setattr(aioredis, "from_url", _from_url)
    yield


@pytest.mark.asyncio
async def test_create_battery_log() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "device_id": "m05",
            "temp_c": 34.2,
            "health": "GOOD",
            "ts": "2025-07-03T10:15:30Z",
        }
        response = await ac.post("/api/v1/battery", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["device_id"] == "m05"
