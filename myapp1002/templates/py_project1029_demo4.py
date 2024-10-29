import datetime


def days_in_month(year: int, month: int) -> int:
    """ inputs: year between datetime.MINYEAR and datetime.MAXYEAR,
        month - integer between 1 and 12  """

    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    # Subtract one day from 1st day of next month
    last_day_month = next_month - datetime.timedelta(days=1)
    return last_day_month.day


# print(days_in_month(2020, 10))  # 31


def is_valid_date(year: int, month: int, day: int) -> bool:
    """ takes input year, month, day and returns True or False if it passes the validity check."""
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


# print(date_is_valid(2024, 10,29))  # True
# print(date_is_valid(2027, 10, 29))  # True
# print(date_is_valid(2024, 10,33))  # False


def days_between(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    """ method to take year2 and subtract year1 to check the days between the two,
        and return the number of days between the two """
    # define local variables
    valid_check1 = is_valid_date(year1, month1, day1)
    valid_check2 = is_valid_date(year2, month2, day2)
    # create datetime objects
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # if statement to check if valid inputs & prints out valid msg
    if not (valid_check1 and valid_check2):  # if not T and T booleans
        return "0 - Invalid dates provided"

    year_diff = date2 - date1
    return year_diff.days


# days1 = days_between(2022, 10,27,2024,10,27)
# print(days1)  # 731


def age_in_days(year: int, month: int, day: int):
    """ inputs : year, month, day for the birthday entry,
        returns age of person as of today or 0 if invalid / future date"""
    # define local variables
    valid_check = is_valid_date(year, month, day)
    # create datetime objects
    today = datetime.date.today()
    date1 = datetime.date(year, month, day)

    if not valid_check:
        return 0



    year_diff = today - date1
    return year_diff.days


# print(age_in_days(2000,1,18))  # 9051  @ 102924'
# print(age_in_days(1998,2,15))  # 9753
# print(age_in_days(1981,5,12))  # 15876




