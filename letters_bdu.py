from polygon import *
"""
t = our turtle
def arch(turt, radius, degrees=360):

at end of function:
  t.heading = 0
  move t into position for next letter
  reset attributes letX and letY to 0, 0

"""

def north(t, size):
  lt(t, 90)
  fd(t, size)

def draw_a(t, size):
  north(t, size)
  """
  northE(t, size)
  southE(t, size)
  west(t, size)
  west(t, size)
  rt(t, 90)
  fd(t, size*2)
  """
  t.heading = 0
  fd(t, spacing)

  t.letX = 0
  t.letY = 0
  

size = 20
spacing = size/4
t.letX = 0
t.letY = 0   
   
draw_a(t, size)
  
wait_for_user()

