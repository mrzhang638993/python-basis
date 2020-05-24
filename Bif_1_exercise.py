# python 内置函数的相关的代码实例
# 判断一个类是另外的一个类的实例
class A:
    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def delSize(self):
        del self.size

    a = property(getSize, setSize, delSize)


a = A()
# 判断一个类是另外的一个类的实例
print(isinstance(a, A))
print(getattr(a, 'x', "属性不存在"))
a1 = A()
a1.a = 8
print(a1.a)
del a1.a


class C:
    def __init__(self, size=10):
        self.size = size

    def getXSize(self):
        return self.size

    def setXSize(self, value):
        self.size = value

    def delXSize(self):
        del self.size

    x = property(getXSize, setXSize, delXSize)


c = C()
print(c.x)
c.x = 12
print(c.x)
