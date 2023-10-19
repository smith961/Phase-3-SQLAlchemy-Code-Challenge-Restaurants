from sqlalchemy import Column, Integer, String, ForeignKey, Table,create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

DATABASE_URL = 'sqlite:///restaurants.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
#Create the tables if they don't exist
Base.metadata.create_all(bind=engine)

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column('customer_id', Integer, primary_key=True)
    first_name = Column('first_name' ,String)
    last_name = Column('last_name', String)
    reviews = relationship('Review', backref='customer')
    restaurants = relationship('Restaurant', back_populates='customers')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # def favourite_restaurant(self):
    #     favorite_restaurant = None
    #     for review in self.reviews:
    #         if review.rating > max_rating:
    #             max_rating = review.rating
    #             favorite_restaurant=review.restaurant
            
    #         return favorite_restaurant

    def add_review(self, restaurant, review):
        review= Review(restaurant = restaurant, rating=rating, customer=self)
        session.add(review)
        session.commit()

    # def delete_reviews(restaurant):
    #     delete_reviews = []

    #     for review in delete_reviews:
    #         if review.restaurant == restaurant:
    #             delete_reviews.append(review)

    #         for review in delete_reviews:
    #             session.delete(review)
    #             session.commit()

    pass


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column('review_id', Integer, primary_key=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customers.customer_id'))
    description = Column('description' ,String)
    restaurants = relationship("Restaurant", back_populates='customer')
   
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.full_name()}: {self.rating} stars"
    
        pass

    def review_restaurant():
        pass
    pass




class Restaurant(Base):
    __tablename__ = 'restaurants'
    restaurant_id = Column('restaurant_id', Integer, primary_key=True)
    name = Column('name' ,String)
    price = Column('price', Integer)
    reviews = relationship('Review', backref='restaurant')
    customers = relationship('Customer',secondary='reviews', back_populates='restaurants')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        review_list = []

        for review in self.reviews:
            name_of_customer = f"(review.customer.first_name {review.customer.last_name})"
            string_review = f"Review for {self.name} by {name_of_customer}: {review.rating} stars"

            review_list.append(string_review)
        return review_list
    
    pass




def find_or_create_customer(first_name, last_name, restaurant):
    customer = session.query(Customer).filter(Customer.first_name == first_name).first

    if customer is None:
        customer = Customer(first_name = first_name, last_name = last_name, restaurant=restaurant)
        session.add(customer)
        session.commit()
        print(f"{first_name} {last_name} added with ID {customer.customer_id}")
    else:
        print(f"'{first_name} {last_name}' already exists with ID")
    
    return customer

#function to create customer instance
def create_customer():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    restaurant = input("Restaurant Name: ")

    find_or_create_customer(first_name,last_name,restaurant)

#Restaurant
#restaurant1= Restaurant(name="KFC Chicken", price=100)
restaurant2= Restaurant(name="sweet sensation", price=50)
restaurant3= Restaurant(name="Mr Biggs", price=200)
restaurant4= Restaurant(name="Dominos", price=400)
restaurant5= Restaurant(name="Dodo Pizza", price=250)

#session.add(restuarant1)
session.add_all([
    restaurant2,
    restaurant3,
    restaurant4,
    restaurant5
])

session.commit()

#TEST FOR OUR METHODS
#CUSTOMERS

    



#session.query(Customer).first().restaurants --- a list of the restaurants for the first customer in the database based on your seed data.
#session.query(Review).first().customer --- should return the customer for the first review in the database.