# ThinkPython exercize 9.7 
def threeDbls(word):
	if len(word) < 6: return False
	letNum = 0
	while letNum < len(word)-5:
		if word[letNum] == word[letNum+1] \
		and word[letNum+2] == word[letNum+3] \
		and word[letNum+4] == word[letNum+5]:
			return True
		letNum += 1
	return False

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if threeDbls(word): print word
fin.close()

"""
bookkeeper
bookkeepers
bookkeeping
bookkeepings
"""
