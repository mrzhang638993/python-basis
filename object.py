# 类对象
# 实例化对象
#  面向对象编程的特点和概念，需要进行关注
#  蓝猫，白猫，黑猫。
#  长，宽,面积，周长，
#  类是一个抽象的概念。类的抽象需要根据具体的实际的需要进行抽象的
#  封装: 对应的是实现将对象的行为和属性进行封装操作，继承：对应的体现的是子类用于父类所有的行为和属性
#  多态：对应的是不同的类对于同样的一个行为提供了不同的实现操作
# 函数和方法的区别:函数和方法没有任何本质的区别。
class Person:
    name = "小甲鱼"

    def printSelf(self, name):
        self.name = name
        print(self.name)


person = Person()
person.printSelf('小甲鱼')


class Rectangle:
    width = 4.0
    length = 5.0

    def setRect(self):
        length = float(input("长:"))
        width = float(input("宽:"))
        self.length = length
        self.width = width

    def getRect(self):
        print("这个矩形的长是:", self.length, "宽是:", self.width)

    def getArea(self):
        print(self.width * self.length)


rect = Rectangle()
rect.getRect()
rect.setRect()
rect.getRect()
rect.getArea()


# 封装
# 继承
# self 代表的是当前对象的引用
# 必须要当前的对象和属性被外部使用的话，可以使用如下的关键字进行————以及——实现相关的封装操作,下面是对应的代码示例
# 多态:不同的类对象对于同样的行为具有不同的实现方式，称之为多态。
class Person:
    __name_ = "mrzhang"  # 对于属性的隐藏

    def getName(self):
        return self.__name_


person = Person()
print(person.getName())


### 私有方法的封装操作实现
class Person1:
    name = 'mrzhang'

    def __getName(self):
        return self.name

    def get(self):
        return self.__getName()


person1 = Person1()
name = person1.get()
print(name)


# 类在实例化之后，对应的一些继承的方式会被调用和实现的。

# 测试类的继承
class MyList(list):
    pass


mylist = MyList();
mylist.append(1)
mylist.append(2)
print(mylist)


# python的魔法方法: 使用双下划线包围的。重写对应的魔法方法对应的可以修改类的一些行为的。
# 常见的魔法方法包括__init__(self,param1,param2),
class Ball:
    # name
    def __init__(self, name):  # 重写模仿方法__init__,需要注意的是init的前面和后面对应的是两个_对应的信息的。
        self.name = name

    def kick(self):
        print("我叫%s,该死的,谁踢我" % self.name)


ball = Ball('土豆')  # 不传递参数的话，对应的会报错的。
ball.kick()
"""
class MyClass:
        name = 'FishC'
        def myFun(self):
                print("Hello FishC!")           
>>> MyClass.name
'FishC'
>>> MyClass.myFun()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    MyClass.myFun()
TypeError: myFun() missing 1 required positional argument: 'self'
>>>
"""


class Ticket:
    def price(self, age, day):
        price = 0
        if day in range(1, 6):  # 1,2,3,4,5代表的是平日的票价
            if age == 1:
                price = 50
            else:
                price = 100
        else:  # 6,7对应的是周末的票价的
            if age == 1:
                price = 60
            else:
                price = 120
        return price


bigTicket = Ticket()
bigTicket1 = Ticket()
price1 = bigTicket.price(0, 2)
price2 = bigTicket1.price(0, 2)
bigTicket2 = Ticket()
price3 = bigTicket2.price(1, 2)
print(price1 + price2 + price3)


# 上面代码出现问题的原因在于以下:1.没有构造对象直接调用类的名称；2.使用类型调用而不是对象来调用实例方法
# python的公有方法和私有方法
class Person:
    name = '小甲鱼'


person = Person()
print(person.name)


class Person1:
    __name = '小甲鱼'  # 定义私有变量


person1 = Person1();  # 定义私有变量
print(person1._Person1__name)  # 私有变量无法进行访问,对应的会报错的。

# python的名字改变和名字重整的技术来实现私有变量的操作的，还是可以访问的，可以采用如下的方式来访问的
# 对应的名字重整之后的变脸是如下的： _类名变量名
import random  as r


class Tortoise:
    def __init__(self):
        self.eng=100
    def setPosition(self,x, y):
        self.x = x
        self.y = y

    def getPostion(self):
        return (self.x, self.y)

    def move(self, direction, power):
        if self.eng == 0:
            print("乌龟体能为0，不能移动，项目结束")
            return;
        if direction == 1:  # 向右移动
            if power == 1:
                if self.x == 10:
                    self.x -= 1
            else:  # power==2
                if self.x == 10:
                    self.x -= 2
                elif self.x == 9:
                    self.x = 9
                else:
                    self.x += 2
            self.eng -= 1
        elif direction == 2:  # 向左侧移动
            if power == 1:
                if self.x == 0:
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if self.x == 0:
                    self.x += 2
                elif self.x == 1:
                    self.x = 1
                else:
                    self.x -= 2
            self.eng -= 1
        elif direction == 3:  # 向上移动
            if power == 1:
                if self.y == 10:
                    self.y -= 1
            else:  # power==2
                if self.y == 10:
                    self.y -= 2
                elif self.y == 9:
                    self.y = 9
                else:
                    self.y += 2
            self.eng -= 1
        else:
            if power == 1:
                if self.y == 0:
                    self.y += 1
                else:
                    self.y -= 1
            else:
                if self.y == 0:
                    self.y += 2
                elif self.y == 1:
                    self.y = 1
                else:
                    self.y -= 2
            self.eng -= 1


class Fish:
    def setPos(self,x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return (self.x, self.y)

    def move(self, direction):
        if direction == 1:  # 向右移动
            if self.x == 10:
                self.x -= 1
        elif direction == 2:  # 向左侧移动
            if self.x == 0:
                self.x += 1
            else:
                self.x -= 1
        elif direction == 3:  # 向上移动
            if self.y == 10:
                self.y -= 1
        else:
            if self.y == 0:
                self.y += 1
            else:
                self.y -= 1


tor = Tortoise()
x = r.randint(0, 10)
y = r.randint(0, 10)
tor.setPosition(x, y)
i = 0
list1 = []  # 放置10条鱼的
for i in range(10):
    fish = Fish()
    x1 = r.randint(0, 10)
    y1 = r.randint(0, 10)
    fish.setPos(x1, y1)
    list1.append(fish)
# 下面开始的是对应的乌龟和鱼的移动比赛
for each in list1:
    # each对应的是一个鱼
    position = each.getPos()
    position1 = tor.getPostion()
    if tor.eng == 0:  # 乌龟死了，游戏结束
        break
    if position == position1:
        tor.eng += 20
        continue
    while not position == position1:
        # 获取鱼的位置的随机数
        direc = r.randint(1, 4)
        each.move(direc)
        # 乌龟移动
        dire1 = r.randint(1, 4)
        power = r.randint(1, 2)
        tor.move(dire1, power)
        position = each.getPos()
        position1 = tor.getPostion()
        if tor.eng == 0:  # 乌龟死了，游戏结束
            break
        if position == position1:
            tor.eng += 20
            continue
