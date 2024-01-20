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
    id = new_user.id
    session.add(new_user)
    session.commit()
    session.close()
    return id

def create_test_reservation( user_info : dict, time : datetime.datetime, ):
    pass


def get_time( reservation_id ) -> (datetime.datetime, datetime.datetime):
    '''
    Get the beginning and end time of a reservation
    '''
    session = Session()
    reservation = session.query(Reservation).filter(Reservation.id == reservation_id).first()
    vehicle_id = reservation.vehicle_id
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id)
    duration = vehicle.duration

    start : datetime.datetime = reservation.start_time
    end = start + datetime.timedelta(hours=duration)

    session.close()

    return start, end

def is_overlaped(start : datetime, end : datetime, reservation_id):
    pass

Base.metadata.create_all(engine)




# info = {
#     "f_name"            : "Maxim",
#     "l_name"            : "Bacar",
#     "email"             : "maximbacar@hotmail.ca",
#     "phone"             : "15143764547",
#     "address"           : "1234 Rue de la paix",
#     "immatriculation"   : "123456789"
# }

# v = {

# }

#create_user("Maxim", "Bacar", "maximbacar@hotmail.ca", "15143764547", "1234 Rue de la paix", "123456789")
