def chop(t):
	t.pop()
	t.pop(0)
	
def middle(t):
	return t[1:len(t)-1]
	
testList = [1,2,3,4,5,6]
chop(testList)
print testList
print middle(testList)