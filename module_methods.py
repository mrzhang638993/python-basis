# 魔法方法的实现和相关的业务逻辑实现
# 描述符号中通过对应的__get__ __set__ __delete__ 对应的完成相关的元素的获取，改变以及删除操作
"""
class MyDes:
    def __get__(self, instance, owner):
        print("getting...")
class Test:
    a = MyDes()
    x = a
test = Test()
 对应的可以采用test.x 以及 test.a 实现对应的getting方法的输入和输出操作
"""
"""
class MyDes:
    def __init__(self, value=None):
        self.val = value
    def __get__(self, instance, owner):
        return self.val - 20
    def __set__(self, instance, value):
        self.val = value + 10
        print(self.val)
class C:
    x = MyDes()
if __name__ == '__main__':  # 该模块被执行的话，执行下边语句。
    c = C()
    c.x = 10
    print(c.x)
对应的输出结果是20 和 0
"""
"""
class MyDes:
    def __init__(self, value=None):
        self.val = value
    def __get__(self, instance, owner):
        return self.val ** 2
class Test:
    def __init__(self):
        self.x = MyDes(3)
test = Test()
print(test.x)  # 对应的是一个MyDes的对象的
print(test.x.val)  # 对应的是一个对象的
"""
"""
按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别做出提醒。
"""
"""
class MyDes:
    def __init__(self, value, name):
        self.name = name
        self.value = value
    def __get__(self, instance, owner):
        print("正在获取变量：" + self.name)
        return self.value
    def __set__(self, instance, value):
        print("正在修改变量:" + self.name)
        self.name = value
    def __delete__(self, instance):
        print("正在删除变量:x")
        print("噢~这个变量没法删除~")
        del self.name
class Test:
    x = MyDes(10, 'x')
test = Test()
print(test.x)
test.x = 8
del test.x
"""
"""
定义一个类实现变量修改的历史的记录操作:MyDes
"""
"""
import time
class Record:
    def __init__(self, value=None, name=None, doc=None):
        self.name = name
        self.doc = doc
        self.value = value
        self.f = open("record1.txt", 'a+')
    def __get__(self, instance, owner):
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被读取"
                     + self.name + "=" + str(self.value) + "\n")
        return self.value
    def __set__(self, instance, value):
        self.value = value
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被修改"
                     + self.name + "=" + str(self.value) + "\n")
    def __delete__(self, instance):
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被删除" + "\n")
        del self.name
        del self.f

class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')
test = Test()
print(test.x)
print(test.y)
test.x = 123
test.y = 1.23
test.y = "i love Fishc.com"
del test.x
del test.y
"""
"""
编写描述符 MyDes，使用文件来存储属性，
属性的值会直接存储到对应的pickle（腌菜，还记得吗？）的文件中。
如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。
#对应的属性文件会存储到对应的文件中进行操作管理和实现的
"""
"""
import os
import pickle
import time
class Record:
    def __init__(self, value=None, name=None, doc=None):
        self.name = name
        self.doc = doc
        self.value = value
        self.f = open("record2.txt", 'a+')
        # 需要根据属性名称生成一个泡菜文件的
        self.pickle_file = open(self.name + ".pkl", 'wb')
    def __get__(self, instance, owner):
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被读取"
                     + self.name + "=" + str(self.value) + "\n")
        return self.value
    def __set__(self, instance, value):
        self.value = value
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被修改"
                     + self.name + "=" + str(self.value) + "\n")
        pickle.dump(self.value, self.pickle_file)
        self.pickle_file.flush()
    def __delete__(self, instance):
        self.f.write(str(self.name) + "  变量于北京时间"
                     + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "被删除" + "\n")
        self.pickle_file.close()
        os.remove(self.name + ".pkl")
        del self.name
        self.f.close()
class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')
test = Test()
print(test.x)
print(test.y)
test.x = 123
test.y = 1.23
test.y = "i love Fishc.com"
del test.x
del test.y
"""
