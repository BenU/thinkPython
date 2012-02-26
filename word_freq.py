from string import *
from bisect import *

# making Dictionary of words
fin = open('words.txt')
dictList = {}
for line in fin:
	word = line.strip().lower()
	dictList[word] = ''
fin.close()

def sortWordCount(words, topWords=10):
	sortedWords = []
	for k, v in words.iteritems():
		insort_left(sortedWords, [v,k])
	count = 1
	print "Top %d words:" % (topWords)
	while count < topWords:
		word = sortedWords[-count][1]
		apperances = sortedWords[-count][0]
		print count, word, apperances
		count += 1
		

def wordCount(fileName):
	fin = open(fileName)
	for line in fin:
		cleanLine = line.strip()
		if (cleanLine[:7] == "Author:"): author = cleanLine[7:].strip()
		if (cleanLine[:6] == "Title:"): title = cleanLine[6:].strip()
		if (cleanLine[:3] == "***") and (cleanLine[-3:] == "***"):
			break

	print author + "'s", title +":",

	words = {}
	unListedWords = []
	#count = 0
	totalWordCount = 0
	for line in fin:
	  line = line.replace('-', ' ')	  
	  cleanLine = line.strip()
	  if (cleanLine[:7] == "*** END"): break
	  lineList = cleanLine.split()
	  for word in lineList:
			cleanWord = word.strip(whitespace + punctuation)
			cleanWord = cleanWord.lower()
			if cleanWord in words: 
				words[cleanWord] += 1
			else:
				words[cleanWord] = 1
				totalWordCount += 1
			if cleanWord not in dictList: unListedWords.append(word)
	fin.close()
	print "Distinct Words:", totalWordCount
	print "Total Unlisted words: ", str(len(unListedWords))
#	for word in unListedWords:
#		print word

wordCount("countOfMC.txt")
wordCount("shakespereCW.txt")
wordCount("davidC.txt")
wordCount("londonJackCoW.txt")
wordCount("kiplingJB.txt")
wordCount("wodehouseJeves.txt")