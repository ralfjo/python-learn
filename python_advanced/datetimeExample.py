import datetime

current = datetime.datetime.now()
print(current)
print(current.year)
print(current.month)
print(current.day)

day_of_week = current.weekday()
print(day_of_week)

custom_date = datetime.datetime(
    year = 2023,
    month = 1,
    day = 1
)
print(custom_date)

datetime_object = datetime.datetime.strptime\
    ("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
print(type(datetime_object))
print(datetime_object)

datetime_str = datetime_object.strftime\
    ("%Y-%m-%d %H:%M:%S")
print(type(datetime_str))
print(datetime_str)

from datetime import timedelta
print(datetime_object + timedelta(days=1))