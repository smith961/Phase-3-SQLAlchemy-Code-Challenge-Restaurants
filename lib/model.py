from sqlalchemy import Column, Integer, String, ForeignKey, Table,create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

DATABASE_URL = 'sqlite:///mydatabase.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# restaurant = Table (
#     'restaurant',
#     Base.metadata,
#     Column('name', String),
#     Column('price', Integer)
# )

# customer = Table (
#     'customer',
#     Base.metadata,
#     Column('first_name', String),
#     Column('Last_name', String)
# )

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name' ,String)
    last_name = Column('last_name', String)
    reviews = relationship('Review', backref='customers')
    restaurants = relationship('Restaurant', back_populates='customers')
    pass


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column('review_id', Integer, primary_key=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customers.customer_id'))
    description = Column('description' ,String)
    restaurants = relationship("Restaurant", back_populates='customers')
   
    def review_customer():
        pass

    def review_restaurant():
        pass
    pass




class Restaurant(Base):
    __tablename__ = 'restaurants'
    restaurant_id = Column('restaurant_id', Integer, primary_key=True)
    name = Column('name' ,String)
    price = Column('price', Integer)
    reviews = relationship('Review', backref='restaurants')
    customers = relationship('Customer', back_populates='restaurants')
    pass


#Create the tables if they don't exist
Base.metadata.create_all(bind=engine)
#session.query(Customer).first().restaurants --- a list of the restaurants for the first customer in the database based on your seed data.
#session.query(Review).first().customer --- should return the customer for the first review in the database.