import os
import json
from fastapi import APIRouter
import redis.asyncio as aioredis

from ..db import async_session
from ..models import BatteryLog
from ..schemas import BatteryLogCreate, BatteryLogRead

router = APIRouter(prefix="/api/v1/battery")


@router.post("", response_model=BatteryLogRead)
async def create_battery_log(payload: BatteryLogCreate) -> BatteryLogRead:
    async with async_session() as session:
        log = BatteryLog(**payload.model_dump())
        session.add(log)
        await session.commit()
        await session.refresh(log)

    redis_url = aioredis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True
    )
    await redis_url.publish(f"battery:{payload.device_id}", json.dumps(payload.model_dump(), default=str))
    await redis_url.close()
    return BatteryLogRead.from_orm(log)
