"""使用python 设计第一个游戏"""

temp=input("不妨猜猜小甲鱼现在心里想的是那个数字: ")
guess=int(temp);

if  guess==8:
    print("你是小甲鱼心里的蛔虫嘛？！")
    print("哼，猜中了也没有奖励！")
else:
    print("猜错了，小甲鱼现在心里想的是8！")
print("游戏结束，不玩了")
