from exc16_1 import Time

def is_after(t1, t2):
  return t1.convert_to_seconds() > t2.convert_to_seconds()
  

t1 = Time()
t1.hour, t1.minute, t1.second = 11, 30, 32

t2 = Time()
t2.hour, t2.minute, t2.second = 11, 30, 31

print is_after(t1,t2)