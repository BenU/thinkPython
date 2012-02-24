import time
from bisect import bisect_left

def in_list(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False

# making List of words
fin = open('words.txt')
wordList = []
for line in fin:
	word = line.strip()
	wordList.append(word)
fin.close()

# making Dictionary of words
fin = open('words.txt')
dictList = {}
for line in fin:
	word = line.strip()
	dictList[word] = ''
fin.close()
	

searchWord1 = 'zebra'
searchWord2 = 'mother'

start = time.time()
if searchWord1 in wordList: print "found searchWord1!"
if searchWord2 in wordList: print "found searchWord2!"
appendTime = time.time() - start
print "in list time: %f" % (appendTime)

start = time.time()
if in_list(wordList, searchWord1) : print "found searchWord1!"
if in_list(wordList, searchWord2) : print "found searchWord2!"
bisectTime = time.time() - start
print "in list time: %f" % (bisectTime)

start = time.time()
if searchWord1 in dictList: print "found searchWord1!"
if searchWord2 in dictList: print "found searchWord2!"
dictTime = time.time() - start
print "in dictionary time: %f" % (dictTime)