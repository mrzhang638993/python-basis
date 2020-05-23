# 构造和析构
class Capstr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(str, string)


# 结构函数的操作逻辑实现,实现对应的构造对象的逻辑
a = Capstr("good")
print(a)

"""
del  析构方法，对象销毁的时候对应的会调用del方法进行销毁操作的。
对应的垃圾回收器进行处理的时候会调用del方法进行对象的销毁操作的
"""


class C:
    def __init__(self):
        print("我是init方法,我被调用了")

    def __del__(self):
        print("我是__del__")


c = C()
# 不是发生del操作的时候，而是垃圾回收器的时候才会对应的进行调用销毁对象的操作的
c.__del__()
c1 = c
c2 = c1
del c1
del c2
del c
