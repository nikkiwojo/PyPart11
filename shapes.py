
class rectangle:

    def __init__(self, x, y):
        self.length = x
        self.width = y

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return ((2 * self.length) + (2 * self.width))


class square(rectangle):

    def __init__(self, x, y):
        rectangle.__init__(self, x, x)






