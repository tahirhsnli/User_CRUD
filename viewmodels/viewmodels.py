from pydantic import BaseModel
from typing import List



class ApplySourceCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ApplySourceResponse(BaseModel):
    applysource_id: int
    name: str

    class Config:
        orm_mode = True

class PositionCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PositionResponse(BaseModel):
    position_id: int
    name: str

    class Config:
        orm_mode = True




