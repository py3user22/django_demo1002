import datetime
from py_is_valid_date1031 import is_valid_date


def days_between(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
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
    """
    # define local variables
    valid_check1 = is_valid_date(year1, month1, day1)
    valid_check2 = is_valid_date(year2, month2, day2)
    # create datetime objects
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # if statement to check if valid inputs & prints out valid msg
    if not (valid_check1 and valid_check2):  # if not T and T booleans
        return 0

    if date1 > date2:
        return 0

    year_diff = date2 - date1
    return abs(year_diff.days)