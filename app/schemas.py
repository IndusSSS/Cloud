from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BatteryLogBase(BaseModel):
    device_id: str
    temp_c: float
    health: str
    ts: datetime


class BatteryLogCreate(BatteryLogBase):
    pass


class BatteryLogRead(BatteryLogBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
