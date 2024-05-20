from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/parking_lots/", response_model=schemas.ParkingLot)
def create_parking_lot(parking_lot: schemas.ParkingLotCreate, db: Session = Depends(get_db)):
    return crud.create_parking_lot(db=db, parking_lot=parking_lot)

@router.get("/parking_lots/{parking_lot_id}", response_model=schemas.ParkingLot)
def read_parking_lot(parking_lot_id: int, db: Session = Depends(get_db)):
    db_parking_lot = crud.get_parking_lot(db, parking_lot_id=parking_lot_id)
    if db_parking_lot is None:
        raise HTTPException(status_code=404, detail="Парковочное место не найдено")
    return db_parking_lot
