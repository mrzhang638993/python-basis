class C:
    def x(self):
        print("x-man")


c = C()
c.x = 10


# 当属性名称和方法名称一致的话，属性会覆盖方法名称的 c.x()
# 尽量的利用组合的机制来扩展类的机制的，还有就是需要组合的

#  python 中的方法需要实例才可以调用的，对应的称之为绑定的
class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x, self.y)

dd = CC()
# 打印出来实例的属性方法
print(dd.__dict__)
# 打印出来CC类实例的属性
print(CC.__dict__)
dd.setXY(4, 5)
print(dd.__dict__)
# 类对象删除之后，对应的由类构建的对象对应的还是存在的。存在于内存中的。
