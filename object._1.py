class MyClass:
    def __init__(self):  # __init__ 方法不能存在返回值
        "I love FishC.com!"


# myclass=MyClass()

# 子类和父类的想法相同的时候，子类重写了父类的方法，父类的方法还是存在的
# 重写父类中的相关的飞行的方法
# super对应的是父类对象的
# 下面的操作逻辑对应的是多重继承导致的问题的，可以使用组合的方式来解决多重继承的操作逻辑和实现特性的
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")


class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")


class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")


class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")


a = A()
b = B()
c = C()
d = D()
