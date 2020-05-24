# python 对象的课后习题的训练
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, z, r):
        self.z = z
        self.r = r

    def getLen(self):
        return math.sqrt(math.pow((self.z.x - self.r.x), 2) + math.pow((self.z.y - self.r.y), 2))


point1 = Point(3, 4)
point2 = Point(5, 6)
line = Line(point1, point2)
print(line.getLen())


# 使用self使用的都是实例对象的属性的，使用类对象对应的都是类对象
class C:
    num = 0

    def __init__(self):
        self.x = 4
        self.y = 5
        C.count = 6


c = C()
# 打印类的属性
print(C.__dict__)
# 打印实例对象的属性
print(c.__dict__)


# 定义类实例进行类的追踪创建了多少类对象的
# 体会出来类对象和实例对象的区别操作
class T:
    count = 0

    def __init__(self):
        T.count += 1

    def getCount(self):
        return T.count

    def __del__(self):
        T.count -= 1


t1 = T()
t2 = T()
t3 = T()
print(T.count)
del t1
del t2
print(T.count)


# 定义栈对象，实现栈常见的操作逻辑,对应的是有顺序的数据结构的
class Stack(list):
    def isEmpty(self):
        return self.count()

    def push(self, x):
        self.append(x)

    def pop(self):
        self.pop(0)

    def top(self):
        return self.__getitem__(0)

    def bootom(self):
        return self.__getitem__(self.count() - 1)


stack = Stack()
print(stack.isEmpty())
