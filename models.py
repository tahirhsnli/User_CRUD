from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# SQLAlchemy Base sınıfı
Base = declarative_base()

# Veritabanı motoru (settings.py'den URL alıyoruz)
from settings import settings
engine = create_engine(settings.DATABASE_URL)

# Oturum (session) oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Tablo Örneği
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Pydantic Veri Modelleri (Giriş ve Çıkış için)
class UserCreate(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # SQLAlchemy objelerini destekler
