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
    today = datetime.date.today()
    # create datetime object for the given input date
    date1 = datetime.date(year, month, day)

    try:
        if not valid_check:
            return 0

    except ValueError:
        return 0

    if date1 > today:
        return 0

    year_diff = today - date1
    return abs(year_diff.days)
