class Parent:
    def hello(self):
        print("正在调用父类的方法")


class Child(Parent):
    pass


class Child1(Parent):
    def hello(self):
        print("正在调用子类的方法")


parent = Parent()
child = Child()
child.hello()
child1 = Child1()
child1.hello()

import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x)


class Goldfish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


# 定义鲨鱼类对象
class Shark(Fish):
    # 重写了父类的方法的话，对应的属性就没有相关的属性了，需要调用父类的方法
    def __init__(self):
        #Fish.__init__(self)  # 使用了父类未绑定的方法，重新对子类进行初始化的操作
        super().__init__() # 调用父类的初始化方法
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想")
            self.hungry = False
        else:
            print("太撑了,吃不下了")


# 初始化鱼，进行鱼的移动操作
fish = Fish()
fish.move()
goldFish = Goldfish()
goldFish.move()
shark = Shark()
shark.move()

#python的多重继承,测试多重继承的操作语法
class Base1:
    def fool(self):
        print("我是fool1,我为Base1代言")

class Base2:
    def fool2(self):
        print("我是fool2,我为Base2代言")

class C(Base1,Base2):
    pass

c=C()
c.fool()
c.fool2()

