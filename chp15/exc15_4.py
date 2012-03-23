from World import World
from exc15_3 import *

class Circle(object):
  """attributes should be center_x, center_y, radius"""
  
def draw_circle(canvas, disc):
  canvas.circle([disc.x,disc.y], disc.radius, disc.color)
#  canvas.circle([-25,0], 70, disc.color)

def draw_rectangle(canvas, rect, color='green4'):
  canvas.rectangle(rect, outline='black', width=2, fill=color)
  
def draw_point(canvas, point, color='black'):
  point_list = [[point.x, point.y], [point.x, point.y]]
  draw_rectangle(canvas, point_list, color)

world = World()
canvas = world.ca(width=500, height=500, background='white')
"""
bbox = [[-150,-100], [150, 100]]
draw_rectangle(canvas, bbox)
canvas.circle([-25,0], 70, outline=None, fill='red')
test_point = Point()
test_point.x = 0.0
test_point.y = 0.0
draw_point(canvas, test_point)
"""
face = Circle()
face.x = 0.0
face.y = 0.0
face.radius = 70.0
face.color = 'blue'
face.outline = None
draw_circle(canvas, face)

plate = Circle()
plate.x = 100.0
plate.y = 120.0
plate.radius = 5.0
plate.color = 'orange'
draw_circle(canvas, plate)

wheel = Circle()

world.mainloop()