# 三元表达式以及断言操作符
#  assert 断言的操作
#  small=x  if  x<y else y
# if not (money < 100) 相当于  if money>=100
#  assert 对应的是断言，事先判断语句结果，可以将问题的出现前置操作
#  python中可以使用如下的语句进行x,y,z变量的快速交换的。
x = 1;y = 2;z = 3
x,y,z=y,z,x
print(x,y,z)

# 下面的语句对应的是比较和返回x,y中的最小值
x=5
y=4
print((x < y and [x] or [y])[0])

# 成员资格运算符: in

#  range对应的是python内置的函数，下面显示的是for循环常见的使用用法
favorite="FishC"
for i in favorite:
    print(i,end=' ')

member=['小甲鱼','小布丁','黑夜','迷途','怡静']
for each in member:
    print(each)
    

range(0,5)  #  0 ,1,2,3,4 
list(range(2,9))     # 2,3,4,5,6,7,8
range(1,10,2)  #  1  3 5  7 9 
for i in  range(1,10,2):
    print(i)
    
# 按照 100 分制，90 分以上成绩为 A，80 到 90 为 B，60 到 80 为 C，60 以下为 D，写一个程序，当用户输入分数，自动转换为ABCD 的形式打印
score=int(input("请输入0——100之间的整数分数"))
if score <60:
    print("D")
elif score>=60 and score<80:
    print("C")
elif  score>=80 and score<90:
    print("B")
else:
     print("A")

# 循环改进，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，因此根据统计规律
score=int(input("请输入0——100之间的整数分数"))
if score>=60 and score<80:
    print("C")
elif  score>=80 and score<90:
    print("B")
elif score<60:
    print("D")
else:
     print("A")

"""
将下面的代码转换成为三元操作符：x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z
"""
#small=if x<y else y
#small=if y<z else z

#  5 次
"""
  for i in 5:
    print('I Love FishC')
存在错误
"""
#  break的主要作用是中断当前循环并跳出循环体结束循环，contine的主要的作用是结束当前进行的本次循环操作，进行当前循环的下一次操作
# range(10)    生成0，1,2,3,4,5,6,7,8,9

 #  提高代码的执行效率
i = 0
string = 'ILoveFishC.com'
while i < len(string):
    print(i)
    i += 1
"""
下面的代码可以使用迭代器的方式进行遍历
i = 0
string = 'ILoveFishC.com'
while i < len(string):
    print(i)
    i += 1
"""
string = 'ILoveFishC.com'
for i  in range(len(string)):
     print(string[i], end=' ')

"""
验证用户密码的方式
用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
"""
password=input("请输入密码:")
count=3
while count>0:
    if password=="FishC.com":
        print("密码正确，进入程序")
        break
    else:
        if  "*" in  password:
            print("密码中不能含有\"*\"!您还有",count,"次机会!",end="")
        else:
            print("密码输入错误!您还有",count,"次机会!",end="")
            count=count-1
        password=input("请输入密码:")

"""
求 100~999 之间的所有水仙花数。
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
需要注意使用地板除的除法进行操作
"""
for i in range(100,1000):
    x=i%10  # 个位数字
    y=i//10%10  # 十位数字
    z=i//100 # 百位数字
    if x ** 3 +y **3 +z **3==i:
         print(i,"是一个水仙花数")

"""
有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
"""
count=0
# 从12个求中选择8个球进行组合操作
for i in range(2,7):
    # 从绿色球中至少可以获得2个球，最多可以获取到6个球
    #  需要判断球的数量。不能够超过3个球
    # 需要循环处理一下
    for j  in range(0,3 if 8-i>=3 else 8-i):
        print(i,j,8-i-j)
        count=count+1
print(count)

        
       
    
    
