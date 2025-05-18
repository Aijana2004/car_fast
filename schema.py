from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CarSchema(BaseModel):
    id: int
    year: int
    odometer: int
    fuel: str
    transmission: str
    drive: str
    type: str