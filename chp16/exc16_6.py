from exc16_1 import Time, print_time
from exc16_5 import time_to_int, int_to_time
import random

def mul_time(time, mult):
  time_secs = time_to_int(time)
  mult_secs = mult*time_secs
  return int_to_time(mult_secs)
  
# make list of times to test
sample_size = 20  
test_time_list = []
count = 0
while count < sample_size:
  x = Time()
  x.hour = random.randint(0, 100)
  x.minute = random.randint(0,59)
  x.second = random.randint(0,59)
  test_time_list.append(x)
  count += 1
  
for time in test_time_list:
  print_time(time)

"""  
a = Time()
a.hour = 1
a.minute = 1
a.second = 1

print_time(a)
print_time()
"""