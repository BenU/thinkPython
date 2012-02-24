columns = 4
rows 		= 5
cWidth 	= 4
rHeight 	= 4
corner 	= "+ "
hBorder =	"- "
vBorder	= "|"

def hLine():
	i = 1
	while i <= columns:
		print corner + hBorder*cWidth,
		i += 1
	print corner
	
def vLines():
	i = 1
	while i <= columns:
		print vBorder + "  "*cWidth + " ",
		i += 1
	print vBorder

def printRowTop():
	hLine()
	for i in range(rHeight):
		vLines()
	
def printGrid():
	for i in range(rows):
		printRowTop()
	hLine()	
	
	
printGrid()
