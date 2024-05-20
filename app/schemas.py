from pydantic import BaseModel

class VehicleBase(BaseModel):
    license_plate: str
    type: str
    is_parked: bool

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int
    parking_lot_id: int

    class Config:
        orm_mode: True

class ParkingLotBase(BaseModel):
    name: str
    location: str
    capacity: int

class ParkingLotCreate(ParkingLotBase):
    pass

class ParkingLot(ParkingLotBase):
    id: int
    vehicles: list[Vehicle] = []

    class Config:
        orm_mode: True
