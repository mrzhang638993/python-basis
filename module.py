# 魔法方法,对应的魔法方法体现的是面向对象编程的操作实现
class Rectangle:
    # 对象初始化操作
    # init 对应的是没有返回值的，不要书写返回值的
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) / 2

    def getArea(self):
        return self.x * self.y


rectangle = Rectangle(4, 5)
print(rectangle.getArea())
print(rectangle.getPeri())

# 对象实例化对用的第一个方法是
print(Rectangle.__new__(Rectangle))
