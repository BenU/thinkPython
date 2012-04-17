import math

"""
# Code used to calculate dementions of left approx-equilateral triangle
end_count = 20000
a = 1
while a < end_count:
  c = math.sqrt(5*(a**2))
  c_int = int(c)
  if (abs(c-c_int) <= 5) and (abs(c_int - (2*a)) <= 5) : print a, c
  a += 1


"""
from World import World

width = 250
height = 250

world = World()
canvas = world.ca(width=width, height=height, background='grey')

left_triangle = [[-56,25], [0, 0], [-56, -25]] 
canvas.polygon(left_triangle, fill='blue')
top_polygon = [[-56,25], [56,25], [56,0], [0,0]]
canvas.polygon(top_polygon, fill='white')
bottom_polygon = [[-56,-25], [56,-25], [56,0], [0,0]]
canvas.polygon(bottom_polygon, fill='red')



world.mainloop()
