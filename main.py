from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db, init_db
from routers.UserRooter import router as users_router
from routers.CityRouter import router as cities_router
from routers.CompanyRouter import router as companies_router
from routers.PositionRouter import router as position_router
app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup():
    await init_db()



app.include_router(users_router)
app.include_router(cities_router)
app.include_router(companies_router)
app.include_router(position_router)