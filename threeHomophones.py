from pronounce import read_dictionary
prDict = read_dictionary()
prDict['oots'] = "OOTTSS"
prDict['twits'] = "TWitts"
#prDict['craws'] = "OOHED"

fin = open('words.txt')
letWords5 = {}
letWords4 = []

# put all 4 and 5 letter words in respective dictionaries
for line in fin:
	word = line.strip()
	if len(word) == 5:
		letWords5[word] = []
	elif len(word) == 4:
		letWords4.append(word)
fin.close()


print len(letWords5)
count = 0

# at this point, letWords4 and letWords5 contains all 4 and 5 letter words, respectively
for word in letWords5:
	if word not in prDict: continue
	word2 = word[1:]
	if word2 not in prDict: continue
	word3 = word[0] + word[2:]
	if word3 not in prDict: continue
	pronounce1 = prDict[word]
	pronounce2 = prDict[word2]
	pronounce3 = prDict[word3]
	if (pronounce1 == pronounce2) and (pronounce1 == pronounce3):
			print "**** " + word
	
# string with first letter removed is string[1:]
# string with 2nd letter removed is string[0] + string[2:]


"""
**** llama
**** scent
**** llano
**** eerie
"""
 