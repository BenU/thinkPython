class Point:
  
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "({0:0d},{1:0d})".format(self.x, self.y)
    
  def __add__(self, other):
    new_point = Point()
    new_point.x = self.x + other.x
    new_point.y = self.y + other.y
    return new_point

if __name__ == '__main__':  
  p = Point(100, 150)
  print p.x, p.y
