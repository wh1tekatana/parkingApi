from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ParkingLot(Base):
    __tablename__ = "parking_lots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    capacity = Column(Integer)

    vehicles = relationship("Vehicle", back_populates="parking_lot")

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String, unique=True, index=True)
    type = Column(String, index=True)
    is_parked = Column(Boolean, default=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))

    parking_lot = relationship("ParkingLot", back_populates="vehicles")
