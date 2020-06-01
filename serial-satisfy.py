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


