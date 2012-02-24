import random

def genBday():
	month = random.randint(1,12)
	max_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, \
							7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	day = random.randint(1,max_days[month])
	return [month, day]
	
def has_duplicates(t):
	for l in t:
		if t.count(l) > 1 : 
			return True
	return False	


numPeople = 56
numerator = 0.0
denominator = 10000

for c in range(denominator):
	bdayList = []
	for i in range(numPeople):
		bdayList += [genBday()]
	if has_duplicates(bdayList): numerator += 1
	
likelihood = (numerator/denominator)*100
print "The likelihood of %d people in a room sharing the same bday is %f percent" % (numPeople, likelihood) 

	