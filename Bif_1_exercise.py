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
a1.setSize(8)
print(a1.getSize())
a1.delSize()
