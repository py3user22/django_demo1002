from py_days_in_month1031 import days_in_month
from py_is_valid_date1031 import is_valid_date
from py_days_between1031 import days_between
from py_age_in_days1031 import age_in_days


print(days_in_month(2024, 10))  # 31
print(days_in_month(2025, 6))  # 30


print(is_valid_date(2024, 6, 17))  # True
print(is_valid_date(2025, 6, 17))  # True
print(is_valid_date(0, 6, 17))  # False -> before year 1

print(days_between(2024, 6, 17, 2020, 5, 20))  # 0 -> 2024 before 2020 order
print(days_between(1999, 6, 17, 2020, 5, 20))  # 7643
print(days_between(2024, 10, 1, 2024, 10, 31))  # 30
print(days_between(2024, 10, 1, 2025, 10, 31))  # 395


print(age_in_days(2000, 1, 18))  # 9053
print(age_in_days(1998, 2, 15))  # 9755
print(age_in_days(1, 1, 21))  # 739169  -> 0 for <=1
print(age_in_days(2029, 2, 15))  # 0 in future
