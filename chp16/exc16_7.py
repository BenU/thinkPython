class Date(object):
  """represents the date.
  attributes: day, month and year."""

month_days = {0:31,1:31,2:28,3:31,4:30, 5:31,\
6:30,7:31,8:31,9:30,\
10:31,11:30,12:31}

"""
Determining leap years:
1) Any year evenly devisible by 4 is a leap year except
2) Any year that is evenly devisible by 100 is not a leap year unless
3) that year is also evenly devisible by 400
"""

def leap_year(year):
  if (year%4 == 0) and ((year%100 != 0) or (year%400 == 0)): 
    return True
  else:
    return False

def format_date(date):
  return "{0:2d}-{1:2d}-{2:2d}".format(date.year, date.month, date.day)

def increment_date(date, n):
  future_date = date  # note that this may need copy/deepcopy module
  if future_date.month == 2:
    if leap_year(future_date.year): 
      month_length = 29
    else:
      month_length = 28
    # month is February and must determin if leap year
  else:
    # month isn't February so no prob...
    month_length = month_days[future_date.month]
  if (n+future_date.day) <= month_length:
    future_date.day += n
  else: # n > remaining days in month
    days_left_in_month = month_length - future_date.day
    n = n - days_left_in_month 
    if future_date.month == 12:
      future_date.year += 1
      future_date.month = 1
    else:
      future_date.month += 1
    future_date.day = 0
    increment_date(future_date, n)
  return future_date
  
date = Date()
date.month = 4
date.day = 21
date.year = 2012

increment = 1000
print format_date(increment_date(date, increment))



