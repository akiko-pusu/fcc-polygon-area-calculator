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

    '''長方形もしくは正方形のオブジェクトを引数に取り、自身の中に何個オブジェクトが入るかを計算'''

    def get_amount_inside(self, shape):
        inside_height = shape.height
        inside_width = shape.width

        # A // B で商を返す
        count_height = self.height // inside_height
        count_width = self.width // inside_width

        return count_height * count_width

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."

        x_result = f"{self.width * '*'}\n"
        result = ""
        for c in range(self.height):
            result += x_result

        return ''.join(result)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# The Square class should be a subclass of Rectangle and inherit methods and attributes.


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    '''正方形面積を求める場合はRectangleを継承するので実装不要'''
    # def get_area(self):

    '''正方形の対角線を求める場合はRectangleを継承するので実装不要'''
    # get_diagonal(self):

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
        self.side = side

    def set_width(self, side):
        super().set_width(side)
        self.side = side

    def set_height(self, side):
        super().set_height(side)
        self.side = side

    '''正方形の4辺の長さを求める場合はRectangleを継承するので実装不要'''
    # def get_perimeter(self):

    def __str__(self):
        return f"Square(side={self.side})"
