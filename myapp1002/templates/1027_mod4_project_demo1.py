import datetime
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

