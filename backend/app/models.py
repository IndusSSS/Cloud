from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class BatteryLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: str
    temp_c: float
    health: str
    ts: datetime
