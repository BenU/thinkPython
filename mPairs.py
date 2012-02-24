words = {}
fin = open('words.txt')
for line in fin:
	word = line.strip()
	if len(word) in words: 
		words[len(word)].append(word)
	else:
		words[len(word)] = [word]
fin.close()

def meta_pair(word1, word2):
	diff_count = 0
	for let_index in range(len(word1)):
		index = let_index-1
		if word1[index] != word2[index]: diff_count += 1
		if diff_count > 1: return False
	if diff_count == 0: return False
	return True 

count = 0
for word_length, word_list in words.iteritems():
	for word in word_list:
		for index in range(len(word_list)):
			if meta_pair(word, word_list[index-1]): 
				count += 1
				print count, word, word_list[index-1]
"""				
exercise 12.4 - 4
234076 photosynthesizes photosynthesises
234077 photosynthesizes photosynthesized
234078 professionalized professionalizes
234079 professionalizes professionalized
234080 rationalizations nationalizations
234081 counterterrorisms counterterrorists
234082 counterterrorists counterterrorisms
234083 internationalized internationalizes
234084 internationalizes internationalized
"""
		
		