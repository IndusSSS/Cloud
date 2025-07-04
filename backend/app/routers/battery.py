from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas
from ..crud import battery as battery_crud
from ..dependencies import get_db

router = APIRouter(
    prefix="/api/v1/battery",
    tags=["battery"],
)

@router.post("", response_model=schemas.BatteryLogRead)
async def create_battery_log(
    log: schemas.BatteryLogCreate, db: AsyncSession = Depends(get_db)
):
    return await battery_crud.create_battery_log(session=db, log=log)
