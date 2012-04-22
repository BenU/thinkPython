from datetime import datetime, date, time, timedelta

# get user's birthday
# print user's current age and the number of days, hours, minutes 
#   and seconds until their next birthday

bday_year = raw_input('What is your birth year? ')
bday_month = raw_input('What is your birth month? ')
bday_day = raw_input('What is your birthday day? ')

first_bday = date(int(bday_year),int(bday_month),int(bday_day))


print "Your birthday is {1:}/{2:}/{0:}!".format(first_bday.year, first_bday.month, first_bday.day)
today = date.today()
age = today - first_bday
print "So you are {0:} years old and...".format(age.days/365)

this_years_bday = date(today.year, first_bday.month, first_bday.day)
next_bday = this_years_bday
if next_bday <= today: 
  next_bday = next_bday.replace(year=today.year + 1)
# wait_time will give us days.  we need to take today's time into 
# account until midnight
midnight = time(0, 0)
# print midnight
next_bday = datetime.combine(next_bday, midnight)
# print next_bday
# print datetime.now()
wait_time = next_bday - datetime.now()
# print wait_time
# print type(wait_time)
# print wait_time.total_seconds()
seconds_til_midnight = wait_time.total_seconds()
m, s = divmod(seconds_til_midnight, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print "You've got {0:0d} days, {1:0} hours, {2:0} minutes and {3:0} seconds ".format(int(d), int(h), int(m), int(s))
print "until your next birthday!"

