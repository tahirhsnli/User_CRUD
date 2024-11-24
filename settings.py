from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str  # Veritabanı bağlantı URL'si

    class Config:
        env_file = "info.env"  # .env dosyasını buradan yüklüyoruz

settings = Settings()
