import datetime


def is_valid_date(year: int, month: int, day: int) -> bool:
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
        if year < 1 or year > 9999:
            return False
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False
