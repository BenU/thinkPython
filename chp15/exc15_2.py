from exc15_1 import *

class Rectangle(object):
  """ represent a rectangle.
      attributes: width, height, corner.
  """

def move_rectangle(rect, dx, dy):
  rect.corner.x += dx
  rect.corner.y += dy
  
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

if __name__ == '__main__':
  print box.corner.x, box.corner.y
move_rectangle(box, 100, 100)
if __name__ == '__main__': print box.corner.x, box.corner.y
