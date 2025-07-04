from sqlmodel.ext.asyncio.session import AsyncSession
from ..models import BatteryLog
from ..schemas import BatteryLogCreate

async def create_battery_log(session: AsyncSession, log: BatteryLogCreate) -> BatteryLog:
    db_log = BatteryLog.from_orm(log)
    session.add(db_log)
    await session.commit()
    await session.refresh(db_log)
    return db_log
