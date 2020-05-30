# 定义摄氏度属性
class Temp:
    def __init__(self, fget=None, fset=None, fdel=None, fdoc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.fdoc = fdoc

    def __get__(self, instance, owner):
        print("调用到了基本的类")
        return self.fget(instance)

    def __set__(self, instance, value):
        print("调用到了基本的类1")
        self.fset(instance, value)

    def __delete__(self, instance):
        print("调用到了基本的类2")
        self.fdel(instance)


class Temperature1:
    def __init__(self):
        self._x = None

    def getX(self):
        print("获取属性的数值信息")
        return self._x

    def setX(self, value):
        print("设置属性的数值信息")
        self._x = value

    def deleteX(self):
        print("删除属性的数值信息")
        del self._x

    x = Temp(getX, setX, deleteX)


# 定义华氏度属性
class Temperature2:
    def __init__(self):
        self._y = None

    def getY(self):
        print("获取属性的数值信息")
        return self._y

    def setY(self, value):
        print("设置属性的数值信息")
        self._y = value

    def deleteY(self):
        print("删除属性的数值信息")
        del self._y

    y = Temp(getY, setY, deleteY)


# 定义温度类，包含了摄氏度和华氏度的属性信息
class Temp:
    y = Temperature2()
    x = Temperature1()


temp = Temp()
temp.x.x = 12
temp.y.y = 36
print(temp.x.x)
print(temp.y.y)
