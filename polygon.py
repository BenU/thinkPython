import math
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, length):
	for i in range(4):
		lt(t) 
		fd(t, length)
		
def polygon(t, length, nSides, arc=360):
	angle = 360.0/nSides
	print angle
	ratio = int(nSides*(arc/360.0))
	print ratio
	for i in range(ratio):
		lt(t, angle)
		fd(t, length)	
		
def circle(t, r, angle=360):
	print angle
	sides = 100
	length = (r*2*math.pi)/sides
	polygon(t, length, sides, angle)
	


radius = 40
fd(bob, radius)
lt(bob, 180)
fd(bob, radius*2)
lt(bob, 180)
fd(bob, radius)
circle(bob, radius, 450)
		
wait_for_user()