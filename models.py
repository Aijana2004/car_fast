from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text, DECIMAL, Enum
from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime
from typing import Optional, List
from database import Base


class Car(Base):
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    year: Mapped[str] = mapped_column(Integer, nullable=False)
    odometer: Mapped[str] = mapped_column(Integer, nullable=False)
    fuel: Mapped[str] = mapped_column(Text)
    transmission: Mapped[str] = mapped_column(String(80))
    drive: Mapped[str] = mapped_column(String(40))
    type:Mapped[str] = mapped_column(String(80))
