from pydantic import BaseModel
from viewmodels.HrViewModels import HrResponse
from viewmodels.CityViewModels import CityResponse
from typing import List

class CompanyCreate(BaseModel):
    name: str
    class Config:
        orm_mode = True

class CompanyResponse(BaseModel):
    company_id: int
    name: str
    hrs: List[HrResponse] = [] 
    cities : List[CityResponse] = []

    class Config:
        orm_mode = True