"""使用python 设计第一个游戏"""
import random 
result=random.randint(1,10)  # 产生随机数
count=3
#python通过缩进的方式实现不同的代码层次结构的
#优化建议：给出具体的数字是否大于还是小于，提供合理化的建议进行操作的
# 提供多次的猜测结果，使用while循环
# 每次运行程序的时候，对应的答案是随机的
while count>0:
    temp=input("不妨猜猜小甲鱼现在心里想的是那个数字: ")  #接收用户的输入，赋值给temp
    guess=int(temp);
    if  guess==result: #注意缩进的位置的，python非常注重缩进操作的
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没有奖励！")
        break
    elif guess>result:
        print("输入的数据大了")
    else:
        print("输入的数据小了")
    count=count-1
print("游戏结束，不玩了")


#随机数获取到种子之后就可以实现复现随机数的，对应的体现出来的是一个伪随机数的。
x=random.getstate()  #对应的获取当前的随机数的种子
print(x)

random.randint(1,10) 
5
random.randint(1,10)
10
random.randint(1,10)
3
random.randint(1,10)
8
random.randint(1,10)
4
random.randint(1,10)
6
random.randint(1,10)
4
random.randint(1,10)
2
random.randint(1,10)
7
random.randint(1,10)
2
random.setstate(x)   #回归原来的随机数种子，可以复现随机数的
random.randint(1,10)
5
random.randint(1,10)
10
random.randint(1,10)
3
