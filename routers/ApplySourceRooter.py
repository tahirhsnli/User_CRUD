from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import ApplySource
from viewmodels.viewmodels import ApplySourceCreate, ApplySourceResponse
from database import get_db

router = APIRouter(
    prefix="/applysource",
    tags=["applysources"]
)

@router.get("/", response_model=list[ApplySourceResponse],operation_id="get_all")
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ApplySource).order_by(ApplySource.applysource_id))
    users = result.scalars().all()
    return users

@router.post("/post", response_model=ApplySourceCreate,operation_id="post")
async def create_user(applySource: ApplySourceCreate, db: AsyncSession = Depends(get_db)):
    new_apply_source = ApplySource(name=applySource.name)
    db.add(new_apply_source)
    await db.commit()
    await db.refresh(new_apply_source)
    return new_apply_source

@router.put('/put/{id}', response_model=ApplySourceCreate,operation_id="put")
async def update_user(id: int, updated_user: ApplySourceCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ApplySource).where(ApplySource.applysource_id == id))
    applySource = result.scalars().first()

    if not applySource:
        raise HTTPException(status_code=404, detail="User not found")

    applySource.name = updated_user.name
    await db.commit()
    await db.refresh(applySource)
    return applySource

@router.delete('/delete/{id}',operation_id="delete")
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ApplySource).where(ApplySource.applysource_id == id))
    applySource = result.scalars().first()

    if not applySource:
        raise HTTPException(status_code=404, detail="Apply Source not found")

    await db.delete(applySource)
    await db.commit()

    return {"message": f"Apply Source with id {id} has been deleted successfully"}
