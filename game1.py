"""使用python 设计第一个游戏"""


count=3
#python通过缩进的方式实现不同的代码层次结构的
#优化建议：给出具体的数字是否大于还是小于，提供合理化的建议进行操作的
# 提供多次的猜测结果，使用while循环
#
while count>0:
    temp=input("不妨猜猜小甲鱼现在心里想的是那个数字: ")  #接收用户的输入，赋值给temp
    guess=int(temp);
    if  guess==8: #注意缩进的位置的，python非常注重缩进操作的
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没有奖励！")
        break
    elif guess>8:
        print("输入的数据大了")
    else:
        print("输入的数据小了")
    count=count-1
print("游戏结束，不玩了")
