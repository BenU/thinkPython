def sumall(*numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum
	
print sumall(1,2,3,4,5)
print sumall(3,4)
print sum((1,2))
print sum((5,6,7))