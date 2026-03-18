
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
