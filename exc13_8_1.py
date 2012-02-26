# arguments: word(with puntuation) and prefixLen=2
# from text file collect prefixLen words with punctuation.
# put prefix in dictionary
# [prefix]: [suffix, number of appearances]
# use exc13_7 to choose random words

import string
import bisect
import random

def process_file(filename, prefixLen=2):
	h = dict()
	fp = open(filename)
	
	longLine = ""

	for line in fp:
		line = line.strip(string.whitespace)
		line = line.replace('--', ' ')
		lineLen = len(line)
		if lineLen == 0: continue
		line = line + " "
		longLine = longLine + line

	# at this point the string is now one long string with each word separated with a space
	words = longLine.split()
	# at this point, the words are all in one lone array
	

	
	endCount = (len(words)-prefixLen)
	# endCount = 1000 # comment out and uncomment line above for real program
	index = 0
	while index < endCount:
		pIndex = index
		prefix = ""
		while pIndex < (index + prefixLen):
			prefix = prefix + " " + words[pIndex]
			pIndex += 1
		suffix = words[pIndex]
		# at this point we've got h{prefix: [[suffix, numberAppearances]]}, the prefix, the suffix
		if prefix in h.keys():
			if suffix in h[prefix].keys():
				h[prefix][suffix] += 1
			else: # no h[prefix]
				h[prefix][suffix] = 1
		else:
			h[prefix] = {}
			h[prefix][suffix] = 1
		index += 1
	return h
	

marcHist =  process_file('londonJackCoW.txt')
marcHistList = []

for k, v in marcHist.iteritems():
	bisect.insort_left(marcHistList, [k, len(v), v])
# marcHistList is a list of [prefix, number of possible suffixes, suffix dictinary[suffix][number of appearances]]		

prefixList = []
for pf in marcHistList:
	bisect.insort_left(prefixList, pf[0])

# now have: marcHistList, prefixList whose indices match up

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else: 
			return -5

def randSuffix(prefix):
	prList = prefix.split()
	prLength = len(prList)
	pr_index = index(prefixList, prefix)
	numSuffixes = marcHistList[pr_index][1]
	suffixDict = marcHistList[pr_index][2]
	if numSuffixes == 1: # ie: there is only one possible suffix
		suffix = marcHistList[pr_index][2].keys()
	else:
		cumAppearances = 0
		appearanceList = suffixDict.values()
		totalAppearances = sum(appearanceList)
		randIndex = random.randint(0,totalAppearances)
		for suf, appearances in suffixDict.iteritems():
			cumAppearances += appearances
			if cumAppearances >= randIndex: 
				suffix = suf
				break
	print suffix,
	prList.pop(0) # remove first word in prefix
	prList.append(suffix)
	newPr = ""
	print prList
	for word in prList:
		newPr += str(word)
	
	return newPr


prefix = (random.choice(marcHistList))[0]
print "first prefix:", prefix

numbWords = 10
for i in range(numbWords):
	prefix = randSuffix(prefix)
