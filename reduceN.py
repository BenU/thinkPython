from bisect import *
words = []
fin = open('words.txt')
for line in fin:
	word = line.strip()
	insort_left(words, word)
fin.close()
insort_left(words, "")

def index(a, x):
    'Locate the leftmost value exactly equal to x OR return -1 if x not in a'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
			return -1

reducibleList = []

def str2List(word):
	sList = []
	for letter in word:
		sList.append(letter)
	return sList
	
def list2str(wordList):
	return "".join(wordList)

def reducible(word):
	if (word == "") or (index(reducibleList, word) != -1) : return True
	if index(words, word) == -1: # ie: word not a word
		return False
	wordLetList = str2List(word)
	for i in range(len(word)):
		letterHold = wordLetList.pop(i)
		childTry = list2str(wordLetList)
		if reducible(childTry):
			insort_left(reducibleList, childTry)
			insort_left(reducibleList, word)
#			print childTry
			return True
		wordLetList.insert(i, letterHold)
	return False
			
for word in words:
	if reducible(word): print word

longest = ""
for word in reducibleList:
	if len(word) >= len(longest) : longest = word
print longest 

# complecting
