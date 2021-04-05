class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_perimeter(self):
    return (self.height + self.width) * 2

  def get_area(self):
    return self.height * self.width

  '''長方形の対角線を求めます'''
  def get_diagonal(self):
    # 三平方の定理から
    # axa + bxb = cxc より c = axa + bxbの平方数
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_amount_inside(self):
    return True

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# The Square class should be a subclass of Rectangle and inherit methods and attributes.
class Square(Rectangle):
  def __init__(self, side):
    self.side = side
    self.width = side
    self.height = side

  def get_area(self):
    return self.side * self.side

  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side

  '''正方形の対角線を求めます'''
  def get_diagonal(self):
    # 平方根は　数値 ** 0.5
    return self.side ** 0.5

  def get_perimeter(self):
    return self.side * 4

  def __str__(self):
    return f"Square(side={self.side})"
