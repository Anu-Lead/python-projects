import calendar

# print(calendar.calendar(2022))

import datetime
from datetime import datetime, timedelta, date, time

print(date.today())
print(datetime.now())

now = datetime.now()
print(now.strftime('%A, %B %d %Y'))

dd = datetime(year=2022, hour=23, day=5, month=2, minute=45)
print(dd)

ddd = datetime.strptime("2022/10/10 10:30", "%Y/%m/%d %H:%M")
print(ddd)


