from pydantic import BaseModel
from datetime import datetime

class BatteryLogBase(BaseModel):
    device_id: str
    temp_c: float
    health: str
    ts: datetime

class BatteryLogCreate(BatteryLogBase):
    pass

class BatteryLogRead(BatteryLogBase):
    id: int

    class Config:
        orm_mode = True
