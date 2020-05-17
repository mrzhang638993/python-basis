#my_list = [1, 2, 3, 4,,] 对应的会报错的
#my_list = [1, 2, 3, 4, 5]
#print(my_list[len(my_list)]) IndexError: list index out of range
#my_list = [3, 5, 1, 4, 2]
#my_list.sorted()  方法异常
# KeyError: 'server'
#my_dict = {'host': 'http://bbs.fishc.com', 'port': '80'}
#print(my_dict['server'])
##def my_fun(x, y):
##        print(x, y)
##my_fun(x=1, y=2)
##f = open('test.txt', 'wt')
##f.write('I love FishC.com!\n')
##f.close()
# 引用外部变量的话，对应的需要进行相关的逻辑处理的
##def my_fun1():    # 引用没有声明的变量
##        global x
##        x= 5
##        def my_fun2():
##                x *= x
##                return x
##        return my_fun2()
##
##my_fun1()()
##try:
##    sum=1+'1'
##    f=open('我是一个什么文件的.txt')
##    print(f.read())
##    f.close()
##except (OSError,TypeError):
##    print("出错了")
#### try ------except--------finally 语句的执行逻辑需要进行判断操作
##try:
##    sum=1+'1'
##except TypeError as reason:
##    print("出错了",reason)
##finally:
##    print("无论如何都是需要执行的操作")
##    

# aise直接发起一个新的异常
def testExcept() :
    try:
        sum=1+'1'
        raise TypeError
    except TypeError as reason:
        print("出错了")
    finally:
        print("最终需要执行的语句")
testExcept()

# 可以，except可以捕获多种类型不同的异常
#  使用except 处理的话，对应的会吞没很多的异常情况的，不利于异常情况的查找和实现。
#  使用 finally 语句块执行相关的操作
try:
    for i in range(3):
        for j in range(3):
            if i==2:
                raise KeyboardInterrupt
            print(i,j)
except KeyboardInterrupt:
    print("退出了")

## except 执行程序优化
import random
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
try:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    if temp.isdigit():
        guess = int(temp)
        while guess != secret:
            temp = input("哎呀，猜错了，请重新输入吧：")
            guess = int(temp)
            if guess == secret:
                print("我草，你是小甲鱼心里的蛔虫吗？！")
                print("哼，猜中了也没有奖励！")
            else:
                if guess > secret:
                    print("哥，大了大了~~~")
                else:
                    print("嘿，小了，小了~~~")
    else:
        raise TypeError
except TypeError as  reason:
    print("出错了","输入类型错误，需要的是数字")
except (EOFError,KeyboardInterrupt) as reason:
    print("输入未结束或者是强行中断异常")
print("游戏结束，不玩啦^_^")
# 定义整形数据的封装的操作和实现逻辑
def int_input():
    while True:
        number=input("请输入一个整数:")
        if number.isdigit():
            break
        else:
            print("出错了,您输入的不是整数!")
int_input()

#文件打开的异常操作处理逻辑，没有文件的话可以创建一个新的文件的        
try:
    #  解决方式，文件不存在的话，对应的创建一个新的文件即可实现错误处理的
    f = open('My_File.txt','a') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    f.close()
#  更加推荐使用下面的语句进行异常处理的
try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals(): # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()
