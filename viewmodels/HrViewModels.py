from pydantic import BaseModel
from typing import Optional

class HrCreate(BaseModel):
    name: str
    surname : str
    company_id : int
    class Config:
        orm_mode = True

class HrResponse(BaseModel):
    hr_id: int
    name: str
    surname : str   
    company_id : Optional[int]
    class Config:
        orm_mode = True
