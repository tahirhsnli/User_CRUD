from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from settings import settings

# Asyncpg ile çalışan async motor
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Async session oluşturucu
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Veritabanı oturumları için bir yardımcı fonksiyon
async def get_db():
    async with async_session() as session:
        yield session

# Veritabanını başlatmak için
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)