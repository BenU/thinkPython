class Date(object):
  """represents the date.
  attributes: day, month and year."""

month_days = {0:31,1:31,2:28,3:31,4:30, 5:31,\
6:30,7:31,8:31,9:30,\
10:31,11:30,12:31}

def format_date(date):
  return "{0:2d}-{1:2d}-{2:2d}".format(date.year, date.month, date.day)
  

def increment_date(date, n):
  future_date = date  # note that this may need copy/deepcopy module
  if (n+future_date.day) <= month_days[future_date.month]:
    future_date.day += n
  else: # n > remaining days in month
    days_left_in_month = month_days[future_date.month] - future_date.day
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
date.month = 1
date.day = 15
date.year = 2012

increment = 15
print format_date(date)

while increment <=450:
  future_date = increment_date(date, 15)
  print format_date(future_date)
  increment += 15


