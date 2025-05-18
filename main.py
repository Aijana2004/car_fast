from fastapi import FastAPI,Depends, HTTPException
from schema import CarSchema
from database import SessionLocal
from models import Car
from typing import List,Optional
from sqlalchemy.orm import Session


car_app = FastAPI(title='CAR FASTAPI')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@car_app.post('/car/create/',response_model=CarSchema)
async def create_car(car: CarSchema, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@car_app.get('/car/',response_model=List[CarSchema])
async def list_car(db: Session = Depends(get_db)):
    return db.query(Car).all()


@car_app.get('/car/{car_id}/',response_model=CarSchema)
async def detail_car(car_id:int,db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail='car not found')
    return car


@car_app.put('/car/{car_id}/',response_model=CarSchema)
async def update_car(car_id:int,car_data: CarSchema,db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail='car not found')

    for car_key,car_value in car_data.dict().items():
        setattr(car,car_key,car_value)

    db.commit()
    db.refresh(car)
    return car


@car_app.delete('/car/car_id}/')
async def delete_car(car_id:int,db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail='car not found')

    db.delete(car)
    db.commit()
    return {'message':'this car is deleted'}