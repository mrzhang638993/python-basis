# python 对象的课后习题的训练
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, z, r):
        self.z = z
        self.r = r

    def getLen(self):
        return math.sqrt(math.pow((self.z.x - self.r.x), 2) + math.pow((self.z.y - self.r.y), 2))


point1 = Point(3, 4)
point2 = Point(5, 6)
line = Line(point1, point2)
print(line.getLen())
