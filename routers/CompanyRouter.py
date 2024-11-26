from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import Company
from viewmodels.CompanyViewModels import CompanyCreate,CompanyResponse
from database import get_db

router = APIRouter(
    prefix="/company",
    tags=["companies"]
)

@router.get("/", response_model=list[CompanyResponse])
async def read_companies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Company).order_by(Company.company_id))
    users = result.scalars().all()
    return users

@router.post("/post", response_model=CompanyCreate)
async def create_company(company: CompanyCreate, db: AsyncSession = Depends(get_db)):
    new_company = Company(name=company.name)
    db.add(new_company)
    await db.commit()
    await db.refresh(new_company)
    return new_company

@router.put('/post/{id}', response_model=CompanyCreate)
async def update_company(id: int, companyCreate: CompanyCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Company).where(Company.company_id == id))
    company = result.scalars().first()

    if not company:
        raise HTTPException(status_code=404, detail="User not found")

    company.name = companyCreate.name
    await db.commit()
    await db.refresh(company)
    return company

@router.delete('/delete/{id}')
async def delete_company(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Company).where(Company.company_id == id))
    company = result.scalars().first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    await db.delete(company)
    await db.commit()

    return {"message": f"User with id {id} has been deleted successfully"}
