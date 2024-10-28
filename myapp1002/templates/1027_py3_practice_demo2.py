import datetime
from datetime import timedelta




"""
1027 practice demo2 -- days in a month, check if data is valid, date differences y1 & y2
"""


def days_in_month(year: int, month: int) -> int:
    """inputs: year between datetime.MINYEAR and datetime.MAXYEAR, month - integer between 1 and 12"""
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    # Subtract one day from 1st day of next month
    last_day_month = next_month - datetime.timedelta(days=1)
    return last_day_month.day


year = 2024
month = 10
print(f"Number of days in {month}/{year}: {days_in_month(year, month)}")  # Number of days in 10/2024: 31


print("----------------------------\n")


def date_is_valid(year: int, month: int, day:int) -> int:
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


date1 = date_is_valid(2024, 10, 27)
print(date1)  # True
date2 = date_is_valid(2024, 10, 35 )
print(date2)  # False


print("----------------------------\n")


def days_between(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:

    # define local variables
    valid_check1 = date_is_valid(year1, month1, day1)
    valid_check2 = date_is_valid(year2, month2, day2)
    # create datetime objects
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # if statement to check if valid inputs & prints out valid msg
    if not (valid_check1 and valid_check2):
        return "0 - Invalid dates provided"

    print(date1, date2)   # 2000-01-18 2024-10-27

    year_diff = date2 - date1
    print("year difference in days from year2 to year1: ")
    return (year_diff.days)














days1 = days_between(2022, 10, 27, 2024, 10, 27)
print(days1)  # your checked out and dates are working
print("________")

print("________")
days3 = days_between(2000, 1, 18, 2024, 10, 27)
print(days3)

print("________")

days2 = days_between(1998, 2, 15, 2024, 10, 27)
print(days2)  # 0





