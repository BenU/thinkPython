import math

class Point(object):
  """ defines a point in 2-D space"""
  
def print_point(p):
  print '(%g, %g)' % (p.x, p.y)
  
def distance(a, b):
  xDelta = a.x - b.x
  yDelta = a.y - b.y
  distance = math.sqrt(xDelta**2+yDelta**2)
  return distance
    
blank = Point()
blank.x = 3.0
blank.y = 4.0

if __name__ == '__main__':
  print_point(blank)

start = Point()
start.x, start.y = 0.0, 0.0
finish = Point()
finish.x, finish.y = 3.0, 4.0
if __name__ == '__main__':
  print distance(start, finish)