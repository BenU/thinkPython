class Time():
  
  def time_to_int(self):
    minutes = self.hour*60 + self.minute
    seconds = minutes*60 + self.second 
    return seconds
    

time = Time()
time.hour = 0
time.minute = 2
time.second = 45

print "There are {0:0d} seconds in that time.".format(time.time_to_int())
