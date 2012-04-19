from exc16_1 import Time, print_time

def increment(time, seconds):
  time.second +=  seconds
  carried_minutes = time.second/60
  time.second = time.second%60
  time.minute += carried_minutes
  carried_hours = time.minute/60
  time.minute = time.minute%60
  time.hour += carried_hours
  
start = Time()
start.hour = 0
start.minute = 0
start.second = 0

increment(start, 46789)
print_time(start)
