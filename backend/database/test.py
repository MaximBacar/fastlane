import datetime

a = datetime.datetime(year=2002, month=4, day=4)
t = datetime.timedelta(days=5)
b = datetime.datetime.now

print(a)
print(a+t)
print(b)