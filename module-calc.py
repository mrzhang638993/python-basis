# 模数运算
class int1(int):
    def __add__(self, other):
        return int.__sub__(self, other)


a = int1('3')
b = int1('4')
print(a + b)


class Rint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


c = Rint(5)
d = Rint(3)
print(c + d)
print(1 + d)  # 执行的是对象的radd操作的，1是不支持任何的操作的，取决于对象的


class Nint1(int):
    def __rsub__(self, other):
        return int.__rsub__(other, self)
        #return int.__rsub__(self, other)


e = Nint1(5)
print(e-3)  # 执行的是a对象的rsub操作逻辑的,对应的是2
print(3-e)  # 对应的是-2的逻辑的，需要顺序问题的话，需要注意对应的顺序
