from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def getArea(self):
        return round(pi * self.r ** 2)

    def getPerimeter(self):
        return round(2 * pi * self.r)

