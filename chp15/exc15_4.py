from World import World
from exc15_3 import *
import color_dict

width = 750
height = 750
# there are less than 28**2 total colors
tot_colors_root = 28
swath_width = width/tot_colors_root
swath_height = height/tot_colors_root

# define upper left hand corner x and y
quadrant_x = -(width/2)
quadrant_y = height/2

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
canvas = world.ca(width=width, height=height, background='white')
"""
# exercise 15.4 and 14.4.1
bbox = [[-150,-100], [150, 100]]
draw_rectangle(canvas, bbox)
canvas.circle([-25,0], 70, outline=None, fill='red')
# exercise 15.4.3
test_point = Point()
test_point.x = 0.0
test_point.y = 0.0
draw_point(canvas, test_point)
"""
if __name__ == '__main__':
  # exercise 15.4.4
  face = Circle()
  face.x = 0.0
  face.y = 0.0
  face.radius = 70.0
  face.color = '#ee30a7'
  face.outline = None
  draw_circle(canvas, face)

  plate = Circle()
  plate.x = 100.0
  plate.y = 120.0
  plate.radius = 5.0
  plate.color = 'orange'
  draw_circle(canvas, plate)

  bbox = [[-150,-100], [150, 100]]
  draw_rectangle(canvas, bbox)

  width = 500
  height = 500
  # there are less than 28**2 total colors
  tot_colors_root = 28
  swath_width = width/tot_colors_root
  swath_height = height/tot_colors_root


world.mainloop()