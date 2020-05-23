# 学习内置函数逻辑和理论
# 内置函数之一：issubClass(class,classinfo),一个类被认为是自身的一个子类的。
class A:
    pass


class B(A):
    pass


# 类认为是其自身的一个子类
print(issubclass(B, A))  # True
print(issubclass(B, B))  # True
#  isInstance(object,classInfo)  检查对应的是否是实例信息
b1 = B()
print(isinstance(b1, B))  # 判断是否是实例对象信息


# 访问对象的属性 hasattr(object,name)
class C:
    def __init__(self, x=0):
        self.x = x


c1 = C()
# 属性名称需要使用字符串的操作的
print(hasattr(c1, 'x'))
#  getattr(object,name,default)
print(getattr(c1, 'x', 1))
# setattr 设置对象的属性信息,对应的没有属性的话，抛出异常提示操作信息
print(setattr(c1, 'x', 13))


# delattr  删除对象中的属性，不存在的话，抛出属性异常
# delattr(c1, 'y')  # 对应的会抛出属性异常的error信息


# property 对应的通过属性设置属性进行操作
class C:
    def __init__(self, size=10):
        self.size = size

    def getsize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size
        # self.__delattr__('size')

    # 根据不同的操作，决定调用的是哪一个函数的。具体的可以实现封装的操作实现的。实现代码隔离实现操作的。
    # 用户使用的话，就可以直接使用x对应的进行操作即可的。
    prop = property(getsize, setSize, delSize)


c1 = C()
print(c1.prop)
print(hasattr(c1, 'prop'))
c1.prop = 19
