from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean

import datetime

engine = create_engine('sqlite:///fastlane.db', pool_size=20, max_overflow=0)
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class Vehicle(Base):
    __tablename__   = 'vehicles'
    id              = Column(Integer, primary_key=True, autoincrement=True)
    type            = Column(String)
    service_price   = Column(Float)
    duration        = Column(Integer)

class Reservation(Base):
    __tablename__   = 'reservations'
    id              = Column(Integer, primary_key=True, autoincrement=True)
    user_id         = Column(Integer)
    vehicle_id      = Column(Integer)
    start_time      = Column(DateTime)
    day             = Column(DateTime)

class User(Base):
    __tablename__   = 'users'
    id              = Column(Integer, primary_key=True, autoincrement=True)
    first_name      = Column(String)
    last_name       = Column(String)
    email           = Column(String)
    phone           = Column(String)
    address         = Column(String)
    immatriculation = Column(String)




def create_user( f_name, l_name, email, phone, address, immatriculation) -> int:
    session = Session()
    new_user = User(first_name=f_name, last_name=l_name, email=email, phone=phone, address=address, immatriculation=immatriculation)
    session.add(new_user)
    session.commit()
    id = new_user.id
    session.close()
    return id


Base.metadata.create_all(engine)

user_id1 = create_user("Maxim", "Bacar", "maximbacar@hotmail.ca", "15141234567", "1234 rue de la paix", "123456789")
user_id2 = create_user("Ihana", "Fahmy", "if@hotmail.ca", "15141234567", "1234 rue de la paix", "123456789")

session = Session()
compact = Vehicle(type="compact", service_price=150.00, duration=0.5)
medium = Vehicle(type="medium", service_price=150.00, duration=0.5)
full = Vehicle(type="full", service_price=150.00, duration=0.5)
class1 = Vehicle(type="class-1", service_price=250.00, duration=1)
class2 = Vehicle(type="class-2", service_price=700.00, duration=2)





r1 = Reservation(user_id=user_id1, vehicle_id=4, start_time=datetime.datetime(year=2023, month=1, day=1, hour=3, minute=30, second=0))
r2 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=30, second=0))
r3 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=33, second=0))
r4 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=33, second=0))
r5 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=33, second=0))
r6 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=33, second=0))
r7 = Reservation(user_id=user_id2, vehicle_id=5,  start_time=datetime.datetime(year=2023, month=1, day=1, hour=2, minute=33, second=0))
session.add(compact)
session.add(medium)
session.add(full)
session.add(class1)
session.add(class2)

session.add(r1)
session.add(r2)
session.add(r3)
session.add(r4)
session.add(r5)
session.add(r6)
session.add(r7)
session.commit()
session.close()