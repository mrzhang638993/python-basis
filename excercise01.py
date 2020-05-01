# python对应的都是跨平台的程序语言的。是一种跨平台的计算机程序设计语言。 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
# IDLE:是Python的集成开发环境
#  *
# python 对应的+ 适合于str和str进行拼接的。不适合str和int之间的拼接操作的。
#  在字符串中引入双引号，推荐使用原始字符串操作
str1=r"i love fishc.com """
print(str1)
# 交互模式计算python 一年的秒数
print(1*365*24*3600)
#  配置python的环境到cmd的环境中即可。


#  exer-2
#  bif  built-in function 内置函数
#  查询内置函数的操作符号
print(dir(__builtins__))
# 不一样，变量名称是区分大小写的。
#  python 中的格式缩进是非常重要的
# 可以如下方式解决的
fishc="i love fishc.com"
print("good morning"==fishc)
# 下面的方式会报错的，可以很好的解决== 以及=的问题的。
#print("good morning"=fishc)
# 进行字符串的拼接操作的。


"""下面是hello.python的脚本"""
name=input("用户请输入姓名:")
print("你好,",name)

"""下面是calc.py的脚本文件"""
number=int(input("请输入1——100之间的数字"))
if  1<=number<=100:
    print("你妹好漂亮")
else:
    print("你大爷好丑")


"""下面是变量和字符串的相关的知识"""
#ABD
# 小甲鱼
#  '520'
#  可以使用原始字符串
print(r"let's go")
# 原始字符串后面输入反斜杠的话，可以如下操作,打印原始字符串后面的反斜杠。
print(r"let's go\\"[:-1])

"""下面是计算一年有多少秒的脚本"""
DaysPerYear=365
HoursPerDay=24
MinutesPerHour=60
SecondsPerMinute=60
print("一年的秒数是:",DaysPerYear*HoursPerDay*MinutesPerHour*SecondsPerMinute)

# 下面是长字符串的另外的一种写法
string = (
"我爱鱼C，\n"
"正如我爱小甲鱼，\n"
"他那呱唧呱唧的声音，\n"
"总缠绕于我的脑海，\n"
"久久不肯散去……\n")


"""改进我们的小游戏"""
#  是死循环，会打印无数字的。
#while 'C':
   # print('我爱鱼C!')
# 10次
i = 10
while i:
    print('我爱鱼C!')
    i = i - 1
# 下面的表达式是等价的
cost=30
print(10 < cost < 50)
print(cost>10 and cost<50)

# python一行中是可以书写多个语句的。
print('I love you');print('very much!') 

#python  当中一个语句也可以换成多行来书写,下面的语法是正确的
print(1<  \
    2 )
#  python的 and 逻辑操作符合c语言中的&& 是一样的
#  and 以及 or的短路逻辑


# 下面是游戏改进，增加3次游戏机会
"""使用python 设计第一个游戏"""
count=0
temp=input("请输入一个整数:")  #接收用户的输入，赋值给temp
guess=int(temp);
while count<2:
    if  guess==8: #注意缩进的位置的，python非常注重缩进操作的
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没有奖励！")
        break
    count=count+1
    temp=input("")  #接收用户的输入，赋值给temp
    guess=int(temp);
print("游戏结束，不玩了")
# 测试梅花功能和实现
i=0
while i<8:
    print(" "*(7-i)+"*"*(8-i)+"\n")
    i=i+1

#  python的数据类型
# bool 代表的是布尔类型，float对应的是浮点类型的数据，str对应的是字符串
# int 对应的是向下取整的
##使用int实现四舍五入
print(int(9.99)+int(9.99*10%10//5))
print(int(9.49)+int(9.49*10%10//5))
# 类型转换,int(),str(),float()
#  解决输入的类型金额输出的类型的区别，放置用户的输入存在较大的问题的。需要注意：数值存在类型，变量也是存在类型的。
type('123')
# 更加推荐使用isinstance进行操作
isinstance('123',str)

# 给下面的输入增加类型判断
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
if not temp.isdigit():
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")

# 判断对应的年份数字是否是闰年
year=input("请输入年份数据")
if year.isdigit():
    destyear=int(year)
    if destyear%4==0 and  not destyear%100==0:
        print("该年份是一个闰年",year)
else:
    print("数据格式输入有问题")

#  python常见的算数操作符
# //  对应的是地板除法的，相当于原来的c语言的/ **对应的是幂运算的符号的。
# 一元操作符的优先级高于二元操作符的优先级，二元操作的优先级高于三元操作符的优先级的。
# 优先级的顺序如下的：幂运算>正负号>算数操作符>比较操作符>逻辑操作符(and or  not)


"""python 常见的运算符的操作，
优先级顺序 not >and > or """
# 需要注意的是地板除的操作
print(3.0 // 2.0)   #  1.0
print(3//2)   # 1
#  a<b<c  等同于 a<b and b<c   0.04
# 判断数字为奇数还是偶数操作，除2取余操作即可。
#  not 的优先级高于 and 和or ,and 的优先级高于or的。
# 运算符的优先级，and的优先级高于or
print(3 or 5 and 0)
#  6
print(3 and 5 + True or False)
#not的优先级高于and
print(0 and not 1 or not 2 and 3 or 4 and not 5)
# 计算结果为为4，需要注意的是and以及or操作的短路特性
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9) # 0 or 0 or 6 or 9


"""
 需要注意python中的自增以及自减等的操作的使用的，python中相关的使用和c以及java语言中时存在区别的。
"""
"""打印0——100之间的所有的奇数"""
i=1
while i<=100:
    print(i)
    i+=2
"""爱因斯坦的阶梯"""
i=1
while True:
    if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
        print("步数是如下的:",i)
        break
    else:
        i +=1


    
