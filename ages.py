def reverseStr(num):
	# num must be 2 digits
	return num[1] + num[0]

mom_age = 21
son_age = 12

pal_count = 1

while mom_age <=100:
	if mom_age == int(reverseStr(str(son_age))):
		print pal_count, mom_age, son_age
		pal_count += 1
	mom_age += 1
	son_age += 1

