# 属性访问的操作方法
class C:
    def __init__(self):
        self.x = 'X-man'


c = C()
print(c.x)
print(getattr(c, 'x', '没有这个属性'))


#  property  可以使用属性的方式访问属性

class C1:
    def __getattribute__(self, item):
        print("getattribute")

    def __getattr__(self, item):
        print("getattr")

    def __setattr__(self, key, value):
        print("setattr")

    def __delattr__(self, item):
        print("delattr")


c1 = C1()
# 执行的第一步是getattribute的相关的操作，
c1.x
c1.x = 1
print(c1.x)


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # 推荐使用基类的方式实现对应的赋值操作的，出现递归异常的时候
            self.__dict__[name]=value
            # self.__setattr__(self,name,value) 存在递归深度过大的问题的
            #super.__setattr__(self, name, value)
            # self.name=value 也存在递归深度过大的问题，对应的原因在于递归调用__setattr__

    def getArea(self):
        return self.width * self.height


ren = Rectangle(10, 15)
print(ren.getArea())
ren.__setattr__('square', 20)
print(ren.getArea())

#property 的原理
