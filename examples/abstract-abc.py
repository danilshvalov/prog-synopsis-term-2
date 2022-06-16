import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def square(self):
        return 0  # можно заменить на pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class EmptyShape(Shape):
    def square(self):
        return super().square()


# s = Shape() # error
r = Rectangle(5, 10)
es = EmptyShape()
print(r.square())  # 50
print(es.square()) # 0
