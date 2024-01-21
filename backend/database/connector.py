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

class User(Base):
    __tablename__   = 'users'
    id              = Column(Integer, primary_key=True, autoincrement=True)
    first_name      = Column(String)
    last_name       = Column(String)
    email           = Column(String)
    phone           = Column(String)
    address         = Column(String)
    immatriculation = Column(String)



def create_user(f_name, l_name, email, phone, address, immatriculation) -> int:
    session = Session()
    new_user = User(first_name=f_name, last_name=l_name, email=email, phone=phone, address=address, immatriculation=immatriculation)
    session.add(new_user)
    session.commit()
    id = new_user.id
    session.close()
    return id

def get_vehicle_id(type : str) -> int:
    session = Session()
    vehicle = session.query(Vehicle).filter(Vehicle.type == type).first()
    id = vehicle.id
    session.close()
    return id
    

def create_reservation(reservation_data : dict):
    session = Session()
    user_id = create_user(reservation_data["f_name"], reservation_data["l_name"], reservation_data["email"], reservation_data["phone"], reservation_data["address"], reservation_data["immatriculation"])
    new_reservation = Reservation(user_id = user_id, vehicle_id = get_vehicle_id(reservation_data['type']), start_time = reservation_data['start_time'])
    session.add(new_reservation)
    session.commit()
    session.close()

# added
def get_fullname(user_id) -> str:
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    f_name = user.first_name
    l_name = user.last_name
    fullname = f"{f_name} {l_name}"
    
    session.close()
    return fullname
    
# added
def get_vehicle_type(vehicle_id) -> str:
    session = Session()
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    vehicle_type = vehicle.type
    
    session.close()
    return vehicle_type

def get_phone_nb(user_id) -> str:
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    phonenb = user.phone
    
    session.close()
    return phonenb


# added
def get_reservations(the_date : datetime.datetime):
    session = Session()
    just_date = the_date.date()
    print(just_date)
    all_reservations = session.query(Reservation).filter(func.DATE(Reservation.start_time) == just_date).all()
    
    list_reservations = []
    
    for reservation in all_reservations:
        start, end = get_reservation_time(reservation.id)
        diction = {
            "full_name" : get_fullname(reservation.user_id),
            "phone_nb" : get_phone_nb(reservation.user_id),
            "type" :get_vehicle_type(reservation.vehicle_id),
            "start" : f"{start.hour}:{str(start.minute).zfill(2)}",
            "end" : f"{end.hour}:{str(end.minute).zfill(2)}"
        }
        list_reservations.append(diction)
        
    
    print(list_reservations)
    session.close()


def get_reservation_time( reservation_id ) -> (datetime.datetime, datetime.datetime):
    '''
    Get the beginning and end time of a reservation
    '''
    session = Session()
    reservation = session.query(Reservation).filter(Reservation.id == reservation_id).first()
    vehicle_id = reservation.vehicle_id
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    duration = vehicle.duration

    start : datetime.datetime = reservation.start_time
    end = start + datetime.timedelta(hours=duration)

    session.close()

    return start, end

def is_overlaped(slot : (datetime.datetime, datetime.datetime), reservation_id):
    '''
    Return if the time slot overlaps a reservation
    '''
    slot_start, slot_end                            = slot
    reservation_time_start, reservation_time_end    = get_reservation_time( reservation_id )

    return slot_end >= reservation_time_start and slot_start <= reservation_time_end

def get_slots(time_slot : (datetime.datetime, datetime.datetime)):
    slots = {
        'compact'   : 0,
        'medium'    : 0,
        'full'      : 0,
        'class-1'   : 0,
        'class-2'   : 0,
        'else'      : 0
    }

    session = Session()
    slot_day = time_slot[0].date()
    reservations = session.query(Reservation).filter(func.DATE(Reservation.start_time) == slot_day).all()
    if len(reservations) > 0:
        for reservation in reservations:
            overlap = is_overlaped(time_slot,reservation.id)
            if overlap:
                vehicle_id = reservation.vehicle_id
                vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
                if slots[vehicle.type] > 0:
                    if slots['else'] < 5:
                        slots['else'] += 1
                else:
                    slots[vehicle.type] += 1
    return slots

def is_slot_valid(time_slot : (datetime.datetime, datetime.datetime), type : str):
    slots = get_slots(time_slot)
    if slots[type] > 0:
        if slots['else'] >= 5:
            return False
        
    return True

Base.metadata.create_all(engine)
