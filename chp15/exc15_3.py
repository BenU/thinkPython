from exc15_2 import *
import copy

def move_copy_rectangle(rect, dx, dy):
  new_box = copy.deepcopy(rect)
  new_box.corner.x += dx
  new_box.corner.y += dy
  return new_box
  
if __name__ == '__main__':
  box = Rectangle()
  box.width = 100.0
  box.height = 200.0
  box.corner.x = 0.0
  box.corner.y = 0.0
  new_box = move_copy_rectangle(box, 130, 130)
  print new_box.corner.x, new_box.corner.y