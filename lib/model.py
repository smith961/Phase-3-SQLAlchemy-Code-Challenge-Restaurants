from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext. declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

restaurant = Table (
    'restaurant',
    Base.metadata,
    Column('name', String),
    Column('price', Integer)
)

customer = Table (
    'customer',
    Base.metadata,
    Column('first_name', String),
    Column('Last_name', String)
)

class Restaurant(Base):
    pass

class Review(Base):
    pass

class Customer(Base):
    pass