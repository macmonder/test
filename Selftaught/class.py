import math


class Circle:
    def __init__(self, r):
        """
        R ist Radius
        :type r: int
        """
        self.r = r

    def get_area(self):
        return self.r ** 2 * math.pi


acircle = Circle(3)
print(acircle.get_area())
