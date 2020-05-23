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
