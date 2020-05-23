# 类之间的组合关系
class Turtle:
    def __init__(self, x):
        self.x = x


class Fish:
    def __init__(self, y):
        self.y = y


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池中总共有乌龟,%d只,小鱼%d条" % (self.turtle.x, self.fish.y))

# 不是直线关系的话，可以使用组合的关系来进行类的组合，直线操作的话对应的使用继承的操作的
pool = Pool(1, 10)
pool.print_num()
