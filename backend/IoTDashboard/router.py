from datetime import datetime, timedelta

from fastapi import APIRouter, Query, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .db import get_db
from .services.jwt import get_auth_user

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "success"}


@router.get("/test_jwt")
async def test_jwt(user: dict = Depends(get_auth_user)):
    return {"status": "Authentication Passed"}


@router.get("/sensors", response_model=list[schemas.Sensor])
async def get_sensors(db: Session = Depends(get_db)) -> list[schemas.Sensor]:
    sensors = db.query(models.Sensor).all()
    return [schemas.Sensor(created_at=datetime.now(), id=sensor.id, name=sensor.name) for sensor in sensors]


@router.post("/sensors", status_code=status.HTTP_201_CREATED)
async def add_sensor(sensor: schemas.Sensor, db: Session = Depends(get_db)):
    try:
        record = models.Sensor(name=sensor.name, created_at=datetime.now())
        db.add(record)
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return {"detail": f"Sensor (id={record.id}) has been sucessfully created."}


@router.get("/events", response_model=list[schemas.Event])
async def get_events(delta: int = Query(default=10, example=10), db: Session = Depends(get_db)) -> list[schemas.Event]:
    lookup_time = datetime.now() - timedelta(minutes=delta)
    events = db.query(models.Event).filter(models.Event.created_at >= lookup_time).all()

    return [
        schemas.Event(
            id=event.id, temperature=event.temperature, created_at=event.created_at, sensor_id=event.sensor_id
        )
        for event in events
    ]
