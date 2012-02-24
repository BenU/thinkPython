def isPalindrome(word, first, last):
	while first <= abs(last):
		if word[first] != word[last]: return False
		first += 1
		last -= 1
	return True

# palNum 				last 4 digits palindrome
# palNum + 1 		last 5 digits palindrome
# palNum + 2 		middle 4 digits palindrome
# palNum + 3 		all 6 digits palindrome


palNumStr = '100000'
# possible that 'last number notation must be express negatively from end of number'
while len(palNumStr) < 7:
	palNum = int(palNumStr)
	palNum1 = palNum + 1
	palNum1Str = str(palNum1)
	palNum2 = palNum + 2
	palNum2Str = str(palNum2)
	palNum3 = palNum + 3
	palNum3Str = str(palNum3)
#	print palNumStr, palNum1Str, palNum2Str, palNum3Str


	if isPalindrome(palNumStr, 2, 5) and \
	isPalindrome(palNum1Str, 1, 5) and \
	isPalindrome(palNum2Str, 1, 4) and \
	isPalindrome(palNum3Str, 0, 5):
		print palNum
		break
	else:
		palNum += 1
		palNumStr = str(palNum)
	
print 'Done!'

	
# answer is 198888




