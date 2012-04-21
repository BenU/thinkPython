from exc16_1 import Time, print_time
from exc16_5 import time_to_int, int_to_time
import random

def mul_time(time, mult):
  time_secs = time_to_int(time)
  mult_secs = mult*time_secs
#  print "***", type(mult_secs), mult_secs, int(mult_secs)
#  print "**", int_to_time(int(mult_secs))
  return int_to_time(int(mult_secs))
  
def av_pace(finish_time, distance):
  # Average pace = Finishing Time/Distance
  # or 
  # Average pace = Finishing Time*(1/Distance)
  ave_pace = mul_time(finish_time, (1/distance))
#  print "type of ave_pace is", type(ave_pace)
  print "{0:2d}:{1:2d}:{2:2d}".format(ave_pace.hour, ave_pace.minute, ave_pace.second)
  return ave_pace
  
  
# make list of times to test
sample_size = 20  
test_time_list = []
count = 0
distance = 10.0
while count < sample_size:
  x = Time()
  x.hour = random.randint(0, 100)
  x.minute = random.randint(0,59)
  x.second = random.randint(0,59)
  test_time_list.append(x)
  count += 1
  
for time in test_time_list:  
  print print_time(time), print_time(mul_time(time, 5))
  print_time(av_pace(time, distance))
  

"""  
a = Time()
a.hour = 1
a.minute = 1
a.second = 1

print_time(a)
print_time()
"""