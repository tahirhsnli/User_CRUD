from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, UserCreate, UserResponse
from database import get_db, init_db

app = FastAPI()

# Veritabanını başlatıyoruz
@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/users", response_model=list[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    result = await db.execute(select(User).order_by(User.id))
    users = result.scalars().all()
    return users

@app.post("/users/post", response_model=UserCreate)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    #db_user = db.query(User).filter(User.email == user.email).first()
    #if db_user:
     #   raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.put("/users/post/{id}" ,response_model=UserCreate)
async def create_user(id: int,updated_user : UserCreate, db: AsyncSession = Depends(get_db)):
    #db_user = db.query(User).filter(User.email == user.email).first()
    #if db_user:
     #   raise HTTPException(status_code=400, detail="Email already registered")
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalars().first()
    user.name = updated_user.name
    user.email = updated_user.email
    await db.commit()
    await db.refresh(user)
    return user

@app.delete('/user/delete/{id}')
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    # Kullanıcıyı sorgula
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalars().first()

    # Kullanıcı bulunamazsa hata döndür
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Kullanıcıyı sil
    await db.delete(user)
    await db.commit()

    return {"message": f"User with id {id} has been deleted successfully"}
