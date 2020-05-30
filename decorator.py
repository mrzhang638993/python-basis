"""
 定义适配器的类型
"""


class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.val

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.val = value

    def __delete__(self, instance):
        print("正在删除变量：", self.name)
        print("噢~这个变量没法删除~")


class C:
    x = MyDes(10, 'x')


c = C()
print(c.x)
c.x = 20
del c.x


class Decorate:
    def __init__(self, fget=None, fset=None, fdel=None, fDoc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.fDoc = fDoc

    def __get__(self, instance, owner):
        print("获取变量的数值")
        return self.fget(instance)

    def __set__(self, instance, value):
        print("开始给变量进行赋值操作")
        self.fset(instance, value)

    def __delete__(self, instance):
        print("删除对象")
        self.fdel(instance)


class Test:

    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def deleteX(self):
        del self._x

    x = Decorate(getX, setX, deleteX)


test = Test()
test.x = 12
print(test.x)
del test.x

