#  装配器正常构建
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.fget(instance)

    def __set__(self, instance, value):
        return self.fset(instance, value)

    def __delete__(self):
        self.fdel(self)

    def getter(self, fget):
        return MyProperty(fget, self.fset, self.fdel, self.doc)

    def setter(self, fset):
        return MyProperty(self.fget, fset, self.fdel, self.doc)

    def deleter(self, fdel):
        return MyProperty(self.fget, self.fset, fdel, self.doc)


class C:
    desc = "amazing desc"

    def __init__(self, _x):
        self._x = _x

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    p = MyProperty(getX, setX, delX, desc)


c = C(13)
c.p = 12
print(c.p)
