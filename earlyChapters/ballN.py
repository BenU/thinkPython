"""
class ball:
	
	def __init__(self, bounces=1):
		self.bounces = bounces
		
	def __str__(self):
		return "boing! "*self.bounces	


b = ball(5)
print	b


def print_lyrics():
	print "I'm a lumberjack and I'm OK."
	print "I sleep all night and I work all day!"
	
def repeatLyrics():
	print_lyrics()	
	print_lyrics()
	
repeatLyrics()
"""

def right_justify(word):
	indent = 70 - len(word)
	print indent*' ' + word

right_justify("scarf")
right_justify("Kelly Murphy Mason")
right_justify("Give a brother a break!  Please")
right_justify("The ends don't always justify the means...")

