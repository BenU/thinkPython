def histogram(s):
	d = dict()
	for c in s:
		d[c] = 1 + d.get(c,0)
	return d
	
def print_hist(h):
	lst = h.keys()
	lst.sort()
	for i in lst:
		print i, h[i]
		
def reverse_lookup(d, v):
	keys = []
	for k in d:
		if d[k] == v: keys += k
	return keys
	
def invert_dict(d):
	inv = dict()
	for key in d:
		val = d[key]
		if inv.setdefault(val, [key]) != [key]:
			inv[val].append(key)		
	return inv

	
letList = histogram('brontosaurus')
print_hist(letList)
print reverse_lookup(letList, 1)
print reverse_lookup(letList, 2)
print invert_dict(letList)