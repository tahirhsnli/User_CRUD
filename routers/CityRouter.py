from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import City
from viewmodels.CityViewModels import CityCreate,CityResponse
from database import get_db

router = APIRouter(
    prefix="/city",
    tags=["cities"]
)

@router.get("/", response_model=list[CityResponse])
async def get_cities(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(City).order_by(City.city_id))
    cities = result.scalars().all()
    return cities

@router.post("/post", response_model=CityCreate)
async def create_city(city: CityCreate, db: AsyncSession = Depends(get_db)):
    new_city = City(name=city.name)
    db.add(new_city)
    await db.commit()
    await db.refresh(new_city)
    return new_city

@router.put('/put/{id}', response_model=CityCreate)
async def update_city(id: int, cityResponse: CityCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(City).where(City.city_id == id))
    city = result.scalars().first()

    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    city.name = cityResponse.name
    await db.commit()
    await db.refresh(city)
    return city

@router.delete('/delete/{id}')
async def delete_city(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(City).where(City.city_id == id))
    city = result.scalars().first()

    if not city:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(city)
    await db.commit()

    return {"message": f"User with id {id} has been deleted successfully"}