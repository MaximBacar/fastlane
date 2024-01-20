from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
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


def get_time( reservation_id ) -> (datetime, datetime):
    '''
    Get the beginning and end time of a reservation
    '''
    session = Session()
    reservation = session.query(Reservation).filter(Reservation.id == reservation_id).first()
    vehicle_id = reservation.vehicle_id
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id)
    duration = vehicle.duration

    start = reservation.start_time
    end = start + datetime.timedelta(hours=duration)

    

    


def is_overlaped(start : datetime, end : datetime, reservation_id):
    pass

Base.metadata.create_all(engine)