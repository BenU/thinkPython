class Time(object):
  """represents the time of day.
  attributes: hour, minute, second"""
  
  def convert_to_seconds(self):
    return (self.hour * 60 *60) + (self.minute * 60) + self.second
    
def print_time(time):
  return "{0:2d}:{1:2d}:{2:2d}".format(time.hour, time.minute, time.second)  
  
if __name__ == "__main__":  
  time = Time()
  time.hour = 00
  time.minute = 1
  time.second = 30

  print print_time(time)
  print "In seconds that's {0:d}".format(time.convert_to_seconds())