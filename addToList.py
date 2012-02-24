import time
start = time.time()
fin = open('words.txt')
wordList = []
for line in fin:
	word = line.strip()
	wordList.append(word)
fin.close()
appendTime = time.time() - start
print "append time: %f" % (appendTime)
print wordList[:10]

start = time.time()
fin = open('words.txt')
wordList = []
for line in fin:
	word = line.strip()
	wordList = wordList + [word]
fin.close()
addListTime = time.time() - start
print "Add to List time: %f" % (addListTime)
print wordList[:10]

# append time: 			0.110425
# Add to List time:	256.521417