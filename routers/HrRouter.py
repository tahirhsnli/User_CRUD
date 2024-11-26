from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import Hr
from viewmodels.HrViewModels import HrCreate,HrResponse
from database import get_db

router = APIRouter(
    prefix="/hr",
    tags=["hrs"]
)

@router.get("/", response_model=list[HrResponse])
async def read_hrs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Hr).order_by(Hr.hr_id))
    hrs = result.scalars().all()
    return hrs

@router.post("/post", response_model=HrCreate)
async def create_company(hr: HrCreate, db: AsyncSession = Depends(get_db)):
    new_hr = Hr(name=hr.name,surname=hr.surname,company_id=hr.company_id)
    db.add(new_hr)
    await db.commit()
    await db.refresh(new_hr)
    return new_hr

@router.put('/post/{id}', response_model=HrCreate)
async def update_company(id: int, hrCreate: HrCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Hr).where(Hr.hr_id == id))
    hr = result.scalars().first()

    if not hr:
        raise HTTPException(status_code=404, detail="Hr not found")

    hr.name = hrCreate.name
    hr.surname = hrCreate.surname
    hr.company_id = hrCreate.company_id
    await db.commit()
    await db.refresh(hr)
    return hr

@router.delete('/delete/{id}')
async def delete_company(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Hr).where(Hr.hr_id == id))
    hr = result.scalars().first()

    if not hr:
        raise HTTPException(status_code=404, detail="Hr not found")

    await db.delete(hr)
    await db.commit()

    return {"message": f"User with id {id} has been deleted successfully"}
