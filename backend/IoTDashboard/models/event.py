from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
