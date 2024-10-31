import datetime
from py_is_valid_date1031 import is_valid_date


def age_in_days(year: int, month: int, day: int) -> int:
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    # define local variables
    valid_check = is_valid_date(year, month, day)
    # create datetime objects for current date
    today = datetime.datetime.now()
    # create datetime object for the given input date
    date1 = datetime.datetime(year, month, day)

    if not valid_check:
        return 0

    if date1 > today:
        return 0


    year_diff = today - date1
    return abs(year_diff.days)
