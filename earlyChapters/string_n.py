def find(str, ch, start=0,stop=-1):
	index = start
	if stop == -1 : stop = len(str)
	while index < stop:
		if str[index] == ch : return index
		else:
			index += 1
	return -1
	
print(str(find("apple", "p")))
print(str(find("apple", "p", 2)))
print(str(find("apple", "p", 3))) 
