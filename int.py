import decimal
# 整数
112234579121621/11235813213455
#浮点数
0.1+0.2

#测试python,浮点数不是百分百精确的，存在精确度的问题的，需要进行关注的。
i=0
while i<1:
   i=i+0.1
   print(i)

#  浮点数的比较
print(0.3==0.1+0.2)

#精确计算浮点数模块计算
a=decimal.Decimal('0.1')
b=decimal.Decimal('0.2')
print(a+b)
c=decimal.Decimal('0.3')
print(a+b==c)

# 科学计数法
#0.00005=e-05

#实部和虚部
x=1+2j
print(x.real)  # 获取实部的数值
print(x.imag)  # 获取虚部的数值




