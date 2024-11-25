from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

Base = declarative_base()

from settings import settings
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ApplySource(Base):
    __tablename__ = "applysources"
    applysource_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class ApplySourceCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ApplySourceResponse(BaseModel):
    applysource_id: int
    name: str

    class Config:
        orm_mode = True

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class CityCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class CityResponse(BaseModel):
    city_id: int
    name: str

    class Config:
        orm_mode = True

class Company(Base):
    __tablename__ = "companies"
    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class CompanyCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class CompanyResponse(BaseModel):
    company_id: int
    name: str

    class Config:
        orm_mode = True

class Position(Base):
    __tablename__ = "positions"
    position_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class PositionCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PositionResponse(BaseModel):
    position_id: int
    name: str

    class Config:
        orm_mode = True