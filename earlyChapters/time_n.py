class Time:
	def printTime(time):
		print str(time.hours) + ":" + \
					str(time.minutes) + ":" + \
					str(time.seconds)
					
	def increment(self, seconds):
		self.seconds += seconds
		
		while self.seconds >= 60:
			self.seconds -= 60
			self.minutes += 1
			
		while self.minutes >= 60:
			self.minutes -= 60
			self.hours += 1
			
	def convertToSeconds(self):
		minutes = (self.hours * 60) + \
							self.minutes
		seconds = (minutes * 60) + \
							self.seconds
		return seconds



	
currentTime = Time()
currentTime.hours = 1
currentTime.minutes = 1
currentTime.seconds = 30

currentTime.printTime()
print("In seconds, that's: " + str(currentTime.convertToSeconds()))

"""
currentTime.printTime()
currentTime.increment(500)
currentTime.printTime()
"""				
