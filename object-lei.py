# python 无处不是对象，到处是对象
#  封装： 数据放到list是数据层面的封装，将代码放到函数中对应的是代码的疯转的，对象是两种的封装的。
#import Turtle
#tt=Turtle() #  创建类对象，函数名约定是小写字母开头.OO 面向对象编程，OOP面向对象编程
#print(tt.color)
# 列表对象,python的列表是对象的
list1=[2,1,7,5,3]
list1.sort()
list1.append(9)
# 对象的特点:  封装(封装了行为),继承
class MyList(list):   # 继承列表
    pass

list2=MyList()  #  实例化列表对象
list2.append(5)
list2.append(3)
list2.append(7)
print(list2)
# 多态: 同一个方法对应的提供不同的行为实现
class A:
    def fun(self):
        print("我是小A")
class B:
    def fun(self):
        print("我是小B......")
a=A()
b=B()
a.fun()
b.fun()

# 下面定义self的参数和定义:  python 的self 类似于 this 的指针。 self 指向的是当前的对象的
class Ball:
    def setName(self,name):
        self.name=name
    def kick(self):
        print("我叫%s,该死的,谁踢我..."  % self.name)
a=Ball()
a.setName("球")
b=Ball()
b.setName("球B")
c=Ball()
c.setName("土豆")
a.kick()  # 隐藏的第一个参数是a的内存地址的。
c.kick()

#  python 的魔法方法，使用双下划线包围的。对象默认继承的方法。
# __init__魔法方法
class Ball:
    def __init__(self,name):  # 重写方法，进行初始化的操作
        self.name=name
    def kick(self):
         print("我叫%s,该死的,谁踢我..."  % self.name)
b=Ball('google')
b.kick()
#  共有和私有：面向对象需要区分公有的和私有的。java和C++中是可以private以及public
class Person:
    name='小甲鱼'

p=Person()
print(p.name)
# python中为了实现变量的私有特征，使用name mangling的机制实现私有化的操作的
# 在python 中定义私有变量，只需要在函数名前面加上"_"两个下划线。那么这个函数或者是变量就是私有的
class Person:
    __name="小甲鱼" # 定义内部变量name,外部是无法访问的,将————下划线的变量修改了变量名称而已的
    # 可以对外提供公有的方式实现内部变量的引用处理的
    def getName(self):
        return self.__name
    
p=Person()
#print(p.__name)   私有变量，外部无法访问
print(p.getName())
#  改变之后的名称是__类型————属性名称
print(p._Person__name)  #前面是一个下划线的，后面是两个下划线的
#  python 的私有是伪私有的，没有权限控制的
# 继承特性:  class 类型(父类型)。一个子类可以继承父类的任何属性和方法

class Parent:
    def hello(self):
        print("正在调用父类的方法")
class Child(Parent):
    pass
p=Parent() #  实例化父类
p.hello()
c=Child()
c.hello()
#  子类中定义与父类同名的方法或者属性，则会自动覆盖父类对应的方法或属性
class Child(Parent):
    def hello(self):
        print("正在调用子类的方法") # 覆盖操作的话,只会影响子类自己的，不会影响父类的特性的
c=Child()
c.hello()






        
        
        
