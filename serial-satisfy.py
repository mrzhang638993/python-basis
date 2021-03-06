# -*- coding: UTF-8 -*-
# 定制容器，实现定制容器需要相关的协议操作的
# 迭代操作和逻辑实现
#  需要相关的代码的实践操作和指导实践操作
"""
1.python基于序列的3个容器是：列表、元组、字符串
"""
"""
2定制不可变容器:只需要重写len，以及getitem方法即可的
class StringLike:
    def __init__(self, value):
        self.value = value
    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        return self.value[item]
strLike = StringLike("good")
print(strLike.__len__())
print(strLike.__getitem__(1))
3.定义容器支持reversed() 内置函数，对应的只需要书写reversed的内置函数的
class StringLike:
    def __init__(self, value):
        self.value = value
    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        return self.value[item]
    def __reversed__(self):
        self.value = self.value[::-1]
4.查询容器容量的方法：
__len__可以查询相关的容器容量的办法的
5.支持容器的读写方法操作：
    根据课堂上的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。这一次我们希望定制的列表功能更加全面一些，比如支持 append()、pop()、extend() 原生列表所拥有的方法。你应该如何修改呢？
要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数
要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注意考虑计数器的对应改变）
对应的实现逻辑是如下的：
class MyList:
    def __init__(self, myList):
        self.myList = [x for x in myList]
        self.count = {}.fromkeys(range(len(myList)), 0)
        # 元素追加到列表的末尾
    def append(self, value):
        self.myList.append(value)
        self.count[len(self.myList) - 1] = 0
    def pop(self):
        value = self.myList.pop()
        print(value)
        self.count.pop(len(self.myList))
    # 扩展原来的元素的数值信息
    def extend(self, extendList):
        self.myList.extend(extendList)
        # 对应的需要追加元素的索引到原来的位置的
        total = len(self.myList)
        for i in range(len(self.count), total):
            self.count[i] = 0
    # 返回对应的元素的访问的次数信息
    def counter(self, index):
        return self.myList.count(index)  # 返回指定索引的元素对应的访问的次数
    #  remove 移除第一个匹配的元素
    def remove(self, value):
        index = self.myList.index(value)
        self.myList.pop(index)
        self.count.pop(index)
    # insert 元素的处理和实现逻辑,在指定的索引位置处增加元素操作
    def insert(self, index, value):
        self.myList.insert(index, value)
        self.count.setdefault(index, 0)
    # 对应的是清除的操作逻辑和实现
    def clear(self):
        self.myList.clear()
        self.count.clear()
    def reverse(self):
        self.myList.reverse()
        # 字典对象的不可反转操作实现,对应的切片逻辑处理实现的，
        # 对应的key可以不变的，当地对应的数值是需要改变的
        for k in self.count:
            if k <= len(self.count) // 2:
                temp = self.count[k]
                self.count[k] = self.count[len(self.count) - k - 1]
                self.count[len(self.count) - k - 1] = temp
            else:
                break
    def getItem(self, key):
        self.count[key] += 1
        return self.myList[key]
myList = MyList([1, 3, 5, 7, 9])
print(myList.count)
myList.append(4)
print(myList.count)
myList.pop()
print(myList.count)
myList.extend([9, 10, 11, 12, 13, 14])
print(myList.myList)
print(myList.getItem(2))
print(myList.count)
print(myList.counter(2))
print(myList.getItem(2))
print(myList.getItem(2))
print(myList.getItem(2))
print(myList.getItem(2))
print(myList.getItem(4))
print("======", myList.myList)
print("======", myList.count)
myList.insert(10, 100)
myList.reverse()
print("======", myList.myList)
print("======", myList.count)
"""
"""
1.迭代对应的是遍历的操作体现的
2.迭代器对应的是一个序列的，可以理解为是一个容器的。
3.迭代器是不能回退的
4.for 判断元素为空的话，对应的只需要获取到迭代器的StopIteration
5.在 Python 原生支持的数据结构中，只有集合可以使用迭代器进行访问操作的
6.体现出来所有的对应的和for循环类似的操作
for each in range(5):
    print(each)
it = iter(range(5))
while True:
    try:
        print(next(it))
    except StopIteration:
        break
# 迭代器输出至今为止的所有的闰年的操作的
class LeapYear:
    def __init__(self):
        self.year = 0
    def __next__(self):
        self.year += 1
        if self.year > 2020:
            raise StopIteration
        else:
            return self.year
    def __iter__(self):
        self.year = 0
        return self
leapYear = LeapYear()
it = iter(leapYear)
while True:
    year = next(it)
    if year >= 2000 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(year)
# 迭代器的操作逻辑和实现逻辑
class MyRev:
    def __init__(self, value):
        self.value = value
        self.begin = len(value) - 1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.value[self.begin]
        if self.begin < 0:
            raise StopIteration
        else:
            self.begin -= 1
            return value
myRev = MyRev('FishC')
for i in myRev:
    print(i, end=' ')
# 下面是生成器的相关的操作
1.携程操作的逻辑实现是如下的：
Python 是通过生成器来实现类似于协同程序的概念：生成器可以暂时挂起函数，并保留函数的局部变量等数据，然后在再次调用它的时候，从上次暂停的位置继续执行下去。
2.生成器所能实现的任何操作都可以由迭代器来代替吗，是对的。生成器死迭代器的一种实现的。
3.是的，都可以。因为生成器事实上就是基于迭代器来实现的，生成器只需要一个 yield 语句即可，但它内部会自动创建 __iter__() 和 __next__() 方法。
4.将一个函数改造为生成器，说白了就是把什么语句改为 yield 语句？对应的是return语句实现的
5.说到底，生成器的最大作用是什么？使得函数可以“保留现场”，当下一次执行该函数是从上一次结束的地方开始，而不是重头再来。
6. 对应的是属于迭代操作的业务逻辑和实现的
def get_primes(number):
    while True:   # 对应的是迭代作用实现的
        if is_prime(number):
            yield number
        number += 1
7. 下面是携程生成器的函数操作逻辑
def myRev(data):
    length = len(data)
    while True:
        if length > 0:
            yield data[length - 1]
            length -= 1
for i in myRev("FishC"):
    print(i, end='')
8.
10 以内的素数之和是：2 + 3 + 5 + 7 = 17，那么请编写程序，计算 2000000 以内的素数之和？
import math
def getPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def prime(number):
    i = 0
    while True:
        if i <= number:
            if getPrime(i):
                yield i
            i += 1
        else:
            break
count = 0
# prime(2000000) 对应的实际上就是一个集合的数据的。对应的是一个迭代器的逻辑实现的
for num in prime(2000000):
    count += num
print(count)
"""


