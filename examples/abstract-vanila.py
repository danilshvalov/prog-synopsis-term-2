class Shape:
    def square(self):
        raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


s = Shape()
r = Rectangle(5, 10)
# print(s.square()) # error
print(r.square()) # 50
