def rotate_word(s, rot):
	rotatedW = ''
	for l in s:
		new_l = chr(ord(l)+rot)
		rotatedW += new_l
	return rotatedW
	
def unRotate_word(s, rot):
	unrotatedW = ''
	for l in s:
		new_l = chr(ord(l)-rot)
		unrotatedW += new_l
	return unrotatedW
	
message = "this is a Very SECRET message!"
print message
coded = rotate_word(message, 13)
print coded
print unRotate_word(coded, 13)
	
