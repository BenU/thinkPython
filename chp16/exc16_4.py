from exc16_1 import Time, print_time

def increment(time, seconds):
  new_time = time
  new_time.second +=  seconds
  carried_minutes = new_time.second/60
  new_time.second = new_time.second%60
  new_time.minute += carried_minutes
  carried_hours = new_time.minute/60
  new_time.minute = new_time.minute%60
  new_time.hour += carried_hours
  return new_time
  
start = Time()
start.hour = 0
start.minute = 0
start.second = 0

print_time(increment(start, 46789))