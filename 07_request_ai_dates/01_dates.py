
# wotks with dates and times python

from datetime import datetime, timedelta

# 1. current date and time
now = datetime.now()

print(f"date and time actual: {now}")

# 2. specific date and time
specific_date = datetime(2026, 12, 25, 12, 0, 0)
print(f"specific date: {specific_date}")

# 3. format date

format_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"format date: {format_date}")


# 4. operations with dates (sum, subtraction, ...)
yesterday = datetime.now() - timedelta(days=1)
print(f"yesterday: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"tomorrow: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"one hour after: {one_hour_after}")


# 5. get individual components from a date

print(f"year: {now.year}")
print(f"month: {now.month}")
print(f"day: {now.day}")
print(f"hour: {now.hour}")
print(f"minute: {now.minute}")
print(f"second: {now.second}")
print(f"microsecond: {now.microsecond}")

# 6. calculate the difference between two dates
date1 = datetime(2026, 12, 25)
date2 = datetime(2026, 12, 26)
difference = date2 - date1
print(f"difference: {difference}")


# 7. set locale for date formatting
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
print(f"format date: {now.strftime('%d/%m/%Y %H:%M:%S')}")