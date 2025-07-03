import os
from fastapi.testclient import TestClient
import redis.asyncio as aioredis
import fakeredis.aioredis

os.environ.setdefault("POSTGRES_URL", "sqlite+aiosqlite:///:memory:")

from app.main import app

client = TestClient(app)


def setup_module(module):
    fake = fakeredis.aioredis.FakeRedis()

    def _from_url(*args, **kwargs):
        return fake

    aioredis.from_url = _from_url


def test_websocket_connect() -> None:
    with client.websocket_connect("/ws/battery?device_id=test") as ws:
        ws.send_text("ping")
        assert ws
