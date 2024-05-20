from sqlalchemy.orm import Session
from . import models, schemas

def get_parking_lot(db: Session, parking_lot_id: int):
    return db.query(models.ParkingLot).filter(models.ParkingLot.id == parking_lot_id).first()

def get_parking_lots(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ParkingLot).offset(skip).limit(limit).all()

def create_parking_lot(db: Session, parking_lot: schemas.ParkingLotCreate):
    db_parking_lot = models.ParkingLot(**parking_lot.dict())
    db.add(db_parking_lot)
    db.commit()
    db.refresh(db_parking_lot)
    return db_parking_lot

def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

def get_vehicles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Vehicle).offset(skip).limit(limit).all()

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate, parking_lot_id: int):
    db_vehicle = models.Vehicle(**vehicle.dict(), parking_lot_id=parking_lot_id)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if db_vehicle is None:
        return None
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
