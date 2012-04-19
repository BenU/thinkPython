from exc16_1 import Time, print_time

def time_to_int(time):
  minutes = time.hour*60 + time.minute
  seconds = minutes*60 + time.second
  return seconds
  
def int_to_time(seconds):
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time 

def increment(time, seconds):
  start_seconds = time_to_int(time)
  end_seconds = start_seconds + seconds
  return int_to_time(end_seconds)
  
if __name__ == "__main__":
  time = Time()
  time.hour = 1
  time.minute = 30
  time.second = 30

  print_time(time)
  print_time(increment(time,3600))  