from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import Position
from viewmodels.viewmodels import PositionCreate,PositionResponse
from database import get_db

router = APIRouter(
    prefix="/position",
    tags=["positions"]
)

@router.get("/", response_model=list[PositionResponse])
async def get_positions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Position).order_by(Position.position_id))
    users = result.scalars().all()
    return users

@router.post("/post", response_model=PositionCreate)
async def create_position(applySource: PositionCreate, db: AsyncSession = Depends(get_db)):
    new_position = Position(name=applySource.name)
    db.add(new_position)
    await db.commit()
    await db.refresh(new_position)
    return new_position

@router.put('/post/{id}', response_model=PositionCreate)
async def update_user(id: int, updated_user: PositionCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Position).where(Position.position_id == id))
    applySource = result.scalars().first()

    if not applySource:
        raise HTTPException(status_code=404, detail="Position not found")

    applySource.name = updated_user.name
    await db.commit()
    await db.refresh(applySource)
    return applySource

@router.delete('/delete/{id}')
async def delete_position(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Position).where(Position.applysource_id == id))
    position = result.scalars().first()

    if not position:
        raise HTTPException(status_code=404, detail="Position not found")

    await db.delete(position)
    await db.commit()

    return {"message": f"Position with id {id} has been deleted successfully"}
