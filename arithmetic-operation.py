# 算数运算的操作符
print(type(len))
print(type(dir))
print(type(int))
print(type(list))


class C:
    pass


# 工厂函数对应的是类对象
print(type(C))

# 对应的是一个对象类型
a = int('123')
# 对应的是一个对象类型
b = int('456')
print(type(a))
print(type(b))
print(a + b)


# 可以重定义对应的内置对象的算法实现相关的算法的重写操作，实现更为复杂的对象操作
# 下面的例子对应的是算法重写的操作的,改写加减算法的操作的
class New_INT(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = New_INT(3)
b = New_INT(5)
print(a + b)
print(a - b)


class Try_int(int):
    def __add__(self, other):
        return int.__add__(self, other)
        # return self + other 注意这样的操作对应的会出现无穷的递归操作的，会出现异常的

    def __sub__(self, other):
        return int.__add__(self, other)
        # 对应的会出现无穷递归操作实现的，会抛出递归异常操作的
        # return self - other


c = Try_int(4)
d = Try_int(6)
print(c + d)
print(c - d)
