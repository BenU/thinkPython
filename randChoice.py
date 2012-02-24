from random import *

def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d
	
def totalVal(d):
	count = 0
	for i in d.itervalues():
		count += i
	return count
	
def findRandKey(d, numb):
	count = 0
	for i in d.iterkeys():
		result = i
		count += d[i]
		if count >= numb: break
	return result
	
t = ['a', 'b', 'b']
h = histogram(t)
print h

totalValues = totalVal(h)
aS = 0
bS = 0
for i in range(100):
	randNumb = randint(0, totalValues)
	if findRandKey(h, randNumb) == 'a':
		print 'a'
		aS += 1
	else:
		print 'b'
		bS += 1
print "Total a's: %d" % (aS)
print "Total b's: %d" % (bS)