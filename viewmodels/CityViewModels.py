from pydantic import BaseModel
from viewmodels.CompanyViewModels import CompanyResponse
from typing import List

class CityCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class CityResponse(BaseModel):
    city_id: int
    name: str
    companies : List[CompanyResponse]
    class Config:
        orm_mode = True