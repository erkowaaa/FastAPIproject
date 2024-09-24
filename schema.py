from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CarListValidate(BaseModel):
    id: int
    category: str
    marka: str
    model: str
    price: int
    year: datetime
    mileage: int
    city: str
    volume: float
    color: str
    country: str
    description: Optional[str] = None


class CarBetValidate(BaseModel):
    id: int
    number: int
    total_number: int
    buy_now: int
    start_date: datetime
    end_date: datetime
