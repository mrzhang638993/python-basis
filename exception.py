# 编程的话，永远不要相信你的用户。他们永远不懂程序的
# 程序的exception
#  异常检测和体现处理，使用try-----except  以及 try------finally
import os
try:
    f=open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except (OSError, TypeError) as reason:
    print("文件出错了",str(reason))
except TypeError as reason:
    print('类型出错了',reason)
# 捕捉任何的异常
except:
    print("出错了")  # 会隐藏异常错误提示的，不建议执行相关的操作的。相当于捕获了所有的异常的
# try 可以和多个except的模式进行捕获和操作管理。except捕获到异常的话，对应的后续的代码就不会执行了
#  try------finally 其中finally对应的是一定要执行的操作的
try:
     f=open('我为什么是一个文件.txt')
     print(f.write('我存在了'))
     i=1+'1'
     f.close()
finally:
     f.close()
# 自定义异常 raise
raise ZeroDivisionError("除数为0异常")

# 丰富的else语句，下面是else 语句操作
def showMaxFactor(num):
    count=num//2
    while count>1:
        if num%count==0:
            print("%d最大公约数是%d",(num,count))
            break
        count -=1
    else:   # 此处else和while 结合，当while执行完成任然没有break的话，执行else语句
        print('%d是一个素数' % num)
num=int(input("请输入一个数:"))
showMaxFactor(num)
# 类似的 for 循环等，也是可以执行上面的else语句的
try:
    print(int('abc'))
except ValueError  as reason:  # 出现异常的情况下，只是执行了except语句的，后续的else不会执行。没有异常的话，会执行else语句的
    print("出错了"+reason)
else:
    print("没有任何异常")

#  with语句进行操作，对于抽象出来的很多的try----except ----等的问题的
try:
     with open('我为什么是一个文件.txt') as f:   #  with 语句会关注文件的状态的，对应的调用f.close的相关的方法的。
         print(f.write('我存在了'))
         i=1+'1'
         f.close()
except  OSError as  reason:
    print("出错了",reason)

