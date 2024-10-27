from datetime import datetime
import calendar


def days_in_month(year: int, month: int) -> int:
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    _, num_days = calendar.monthrange(year, month)
    return num_days


year = 2024
month = 10
print(f'Number of days in {month}: {days_in_month(year, month)}')
print("---------------------------\n")


def is_valid_date(year: int, month: int, day: int):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


check1 = is_valid_date(2024,10,27)
print(check1)
check2 = is_valid_date(2024,10,50)
print(check2)
print("---------------------------\n")


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.

      --> should return # of days from year1 date to year2 date.

    """
    date1 = datetime(year1, month1, day1)
    date_valid = is_valid_date(year1, month1, day1)
    date2 = datetime(year2, month2, day2)
    date_valid2 = is_valid_date(year2, month2, day2)
    difference = date2 - date1

    if not (date_valid and date_valid2) and (date1 and date2):
        return 0
    else:
        return abs(difference.days)



check3 = days_between(2024, 10, 27, 2024, 10, 27)
print(check3)
check4 = days_between(2024, 10, 30, 2024, 12, 30)
print(check4)
check5 = days_between(2024, 10, 40, 2024, 10, 30)
print(check5)




