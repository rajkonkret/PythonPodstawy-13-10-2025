from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-10-14
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-10-14 12:55:55.585345
print(type(time))

print(time.year)
print(time.day)
# 2025
# 14
# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-10-15

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_date)  # Sformatowana data: 14/10/2025

# 13:03
# 01:03 pm
formated_time = datetime.now().strftime("%H:%M")
print("Sformatowany czas:", formated_time)  # Sformatowany czas: 13:05
print(type(formated_time))  # <class 'str'>

formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Sformatowany czas usa:", formated_time_usa)  # Sformatowany czas usa: 01:07 PM

# zamiana stringa na typ datetime
object_time = datetime.now().strptime("14/10/2025", "%d/%m/%Y")
print(object_time)  # 2025-10-14 00:00:00
print(type(object_time))  # <class 'datetime.datetime'>

print(35 * "-")
