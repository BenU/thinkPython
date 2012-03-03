import urllib
import re

print "Welcome!"
zipcode = ""
while True:
	zipcode = raw_input('What zip are you interested in? (type done to finish): ')
	if (zipcode == 'done') or (zipcode == 'Done'): break
	zipurl = 'http://www.uszip.com/zip/' + zipcode
	conn = urllib.urlopen(zipurl) 
	for line in conn.fp:
		line = line.strip()
		if re.search("is the zip code of", line) != None:
			leftStripString = "<h1><span class=\"hdn\" style=\"font-size:21px;>" + zipcode + "</span> is the zip code of <strong>"
			rightStripString = "</strong></h1><br>"
			name = line.lstrip(leftStripString).rstrip(rightStripString)
		if re.search("Population:", line) != None: 
			popRight = line.lstrip('<td class="dsc"><b>Population:</b></td><td>')
			rCut = popRight.rfind('<span style')
			population = popRight[:rCut]
	print
	print "The name of that zip is: \t", name
	print "Population: \t\t\t", population
	print

	
