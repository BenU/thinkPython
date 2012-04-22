# get current date and prints day of the week

from datetime import date

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

today = date.today()
print "Today's date is {1:}/{2:}/{0:} and the day of the week is {3:}.".format(today.year, today.month, today.day, days[today.weekday()])
