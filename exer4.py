# 3 < = 4  其中< =是不能分隔的
# 3 <= 5 >= 4  对应的结果是TRUE
print(3 <= 5 >= 4)
print(1 + 1 >= 2)

#代码存在的问题如下：
temp=input("输入变量guess的数值")
guess=int(temp)
if guess == 8:
    print("你是小甲鱼心里的蛔虫嘛？！")
    print("哼，猜中了也没奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
"""
1.缩进没有对齐，存在语法错误
2.变量guess没有定于
"""

# ACD
print('FishC' == '''FishC''')
print(520 == int(520.1314))
print(9 == int(9.99))


#动手编程题
"""
存在的错误：
1.inut对应的是字符串的，需要转换成为数值的
"""
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

if num1 < num2:
    print("第一个数比第二个数小！")

if num1 > num2:
    print("第一个数比第二个数大！")

if num1 == num2:
    print("第一个数和第二个数一样大！")
