import fractions 
# python支持链式比较
# 区别在于 250作为比较表达式的话，最终计算的结果是True的，而bool是可以直接给出表达式的布尔值True或者是False
#  是的，python中所有的对象都是可以进行真值检测的。
#  True  首先计算3==5
print(not 3==5)
print(3==5)
#  是的，布尔值的存储是数值型的。
#  1
print(fractions.Fraction(1, 2) * 2)
# 获取到的是有理数约分之后的数值
print(fractions.Fraction(1708227363155544,4636617128565048))


#  写一个年份，判断是否是闰年
year=int(input("请输入一个年份数据"))
if year%4==0 and year%100!=0:
    print(year,"年是普通闰年")
elif year%10==0 and year%400==0:
    print(year,"年是世纪闰年")
