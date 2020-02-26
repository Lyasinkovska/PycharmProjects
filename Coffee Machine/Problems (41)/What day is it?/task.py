import datetime as dt
import calendar

time = int(input())
day = list(calendar.day_name)
day_number = dt.date.weekday(dt.date.today())

if time < 0:
	print(day[day_number - 1])
elif time > 12:
	print(day[day_number + 1])
else:
	print(day[day_number])






