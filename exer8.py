# 1.6666666666666665
print(1+2/3)
#1
print(1+2//3)
# 被除数不能为0
# 需要考虑算法的优先级
# 1.4
print(1 +- 2 -+ 3 *-4 /+ 5);
# 3 ** 4 %5  =1 
print(pow(3,4,5))
# x=(x // y) * y + (x % y)

##使用int实现四舍五入
print(int(9.99)+int(9.99*10%10//5))
print(int(9.49)+int(9.49*10%10//5))

#计算1000000之内所有偶数的和
i = 0
sum=0
while i <= 1000000:
    sum=sum+i
    i = i + 2
print("1000000之内所有偶数的和是 ",sum)


### 计算麦粒的数量
i=1
count=1
sum=0
while count<=64:
    sum=sum+i
    i=i*2
    count=count+1
print("舍罕王应该给达依尔 ",sum," 粒麦子")

