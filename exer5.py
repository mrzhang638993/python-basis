# NO
#  无限多个
#  无数多个
"""
存在如下的问题：
1.age对应的是字符串，需要转化为数值
2.逻辑存在问题
"""
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年^o^")
else:
    print("对不起，你还未成年T_T")

#  死循环的修改
i=0
while i<1:
    print("iloveFishC.com")
    i=i+1

#  代码补全
x = input("请输入一个数字：")
x = int(x)

if x > 20:
    print("大于20")
else:
    if x < 10:
        print("小于10")
    else:
        print("大于等于10，小于等于20")


#评定分数等级程序,书写&&  还存在问题的
score=int(input("请输入你的考试成绩"))
if score<60:
    print("D")
elif score>=60 and score<80:
    print("C")
elif score>=80 and score<90:
    print("B")
elif  score>=90 and score<100:
    print("A")
elif  score==100:
    print("S")

        
