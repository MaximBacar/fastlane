import datetime

a = datetime.datetime(year=2002, month=4, day=4)
t = datetime.timedelta(days=5)
b = datetime.datetime(bour = 2, min = 37)
c = datetime.datetime.now().time

print(a)
print(a+t)
print(b)
print(c)
print(type(t))
# ///////

# info = {
#     "f_name"            : "Maxim",
#     "l_name"            : "Bacar",
#     "email"             : "maximbacar@hotmail.ca",
#     "phone"             : "15143764547",
#     "address"           : "1234 Rue de la paix",
#     "immatriculation"   : "123456789"
# }
# //////


# v = {

# }
#///////

# create_user("Maxim", "Bacar", "maximbacar@hotmail.ca", "15143764547", "1234 Rue de la paix", "123456789")
#//////


# def addVehicle(t, sp, d):
#     session = Session()
#     vehicle1 = Vehicle(type = t, service_price =sp, duration = d)
#     session.add(vehicle1)
#     session.commit()
#     session.close()
#////////////

# def removeVehicle(id):
#     session = Session()
#     vehicle=  session.query(Vehicle).filter(Vehicle.id == id)
#     vehicle.delete()
#     session.commit()
#     session.close()
    
# removeVehicle(2)
#/////////


# addVehicle("compact", 150, 30)
#//////

# session1 = Session()
# compact_vehicle = Vehicle(type = "compact", service_price = 150, duration= 30)
# session1.add(compact_vehicle)
# session1.commit()
# session1.close()

# id = create_user("Ihana", "Fahmy", "ihanafahmy@hotmail.ca", "15143764547", "1234 Rue de la paix", "123456789")
# create_reservation(id, datetime.datetime.today())

# def create_test_reservation( user_info : dict, time : datetime.datetime ):
