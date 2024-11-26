from sqlalchemy import Table,Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()

from settings import settings
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ApplySource(Base):
    __tablename__ = "applysources"
    applysource_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Position(Base):
    __tablename__ = "positions"
    position_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

city_company = Table(
    'city_company',
    Base.metadata,
    Column('city_id', Integer, ForeignKey('cities.city_id'), primary_key=True),
    Column('company_id', Integer, ForeignKey('companies.company_id'), primary_key=True)
)

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    companies = relationship("Company", secondary=city_company, back_populates="cities")

    

class Company(Base):
    __tablename__ = "companies"
    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hrs = relationship("Hr", back_populates="company",lazy="selectin")
    cities = relationship("City", secondary=city_company, back_populates="companies")
    
class Hr(Base):
    __tablename__ = "hr"
    hr_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    company_id = Column(Integer, ForeignKey('companies.company_id'))
    company = relationship("Company", back_populates="hrs")
    # Relationship

