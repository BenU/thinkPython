def cumList(origList):
	cumList = []
	for c in range(len(origList)):
		cumList.append(sum(origList[:c+1]))
	return cumList
	
	
t = [1,2,3,4]
print t
print cumList(t)