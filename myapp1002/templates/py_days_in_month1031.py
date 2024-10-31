import datetime


def days_in_month(year: int, month: int) -> int:
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    # Subtract one day from 1st day of next month
    last_day_month = next_month - datetime.timedelta(days=1)
    return last_day_month.day