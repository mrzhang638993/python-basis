# 语法错误
#print(3 == not 5)
# 运算符的优先级，and的优先级高于or
print(3 or 5 and 0)
#  6
print(3 and 5 + True or False)
#not的优先级高于and
print(0 and not 1 or not 2 and 3 or 4 and not 5)
#False
print(1 == 2 < 3)
#False
print(1 < 2 > 3 < 4 < 5)

#编程题目
#x%2==1
#x%3==2
#x%5==4
#x%6==5
#x%7==0
#  119
i=0
while True:
    if i%2==1 and i%3==2 and i%4==3 and i%5==4 and i%6==5 and i%7==0:
        print(i)
        break
    else:
        i=i+1

