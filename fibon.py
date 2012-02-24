from time import time

def methodTime(meth, n):
	start = time()
	methRet = meth(n)
	done = time()
	methTime = done - start
	return [methRet, methTime]

def fibonRec(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		rec = fibonRec(n-1) + fibonRec(n-2)	
	
	return rec

known = {0:0, 1:1}
	
def fibonMemo(n):
	if n in known:
		return known[n]
	val = fibonMemo(n-1) + fibonMemo(n-2)
	known[n] = val
	return val

number = 50
fibon50 = fibonMemo(number)
print fibon50
print type(fibon50)
	

	

