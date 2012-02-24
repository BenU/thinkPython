def uses_only(word, letters):
	for l in word:
		if l not in letters:
			return False
	return True
	
def uses_all(word, letters):
	letArray = []
	for l in letters:
		letArray += l
	for l in word:
		if l in letArray: letArray.remove(l)
		if letArray == []: return True
	return False
	
vowels = 'aeiouy'
fin = open('words.txt')
wordCount = 0
for line in fin:
	word = line.strip()
	if uses_all(word, vowels):
		wordCount += 1 
		print word
fin.close()
print "Total:" + str(wordCount)

# there are 598 words that use all of 'aeiou'
# there are 42 words that use all of 'aeiouy'
