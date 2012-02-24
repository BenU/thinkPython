import itertools

def has_no_e(word):
	for l in word:
		if l == 'e' or l == 'E' : return False
	return True

def avoids(word, letters_to_avoid):
	word = word.lower()
	letters_to_avoid = letters_to_avoid.lower()
	for l in word:
		if letters_to_avoid.find(l) != -1: return False
	return True

lowCount = 113809
lowString = ""

alphaBet = 'abcdefghijklmnopqrstuvwxyz'
letCombos = itertools.combinations(alphaBet, 5)
for lets in letCombos:
	avoidString = ''.join(lets)
	fin = open('words.txt')
	word_count = 0
	for line in fin:
		word = line.strip()
		if avoids(word, avoidString): 
			word_count += 1
		if word_count > lowCount : break
	fin.close()
	if word_count <= lowCount:
		lowCount = word_count
		lowString = avoidString
		print avoidString,
		print lowCount

"""
As of 2012-02-17, 22:14
abcde 7990
abceg 6373
abcei 3559
abego 3461
abeil 3334
abeio 1150
aceio 1114
aehio 1110
aeilo 1021
aeior 954
aeios 602
aeiou 107
"""

		



	
