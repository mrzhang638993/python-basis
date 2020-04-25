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


###int类型的操作
#对应的是向下取整的操作的。对应的操作是获取比目标结果小的整数
print(3//2)
# 对应的是1.5
print(-3/-2)
# -2的数值结果
print(-3/2) 
# 3/2=1.5 和java等的不是一样的。
#(1,1)
print(divmod(3,2))
#(-2,1),这个取余数需要关注
print(divmod(-3,2))

#  -x 表示的是获取x的相反数，+x表示的是获取x本身
#  获取绝对值,3 
print(abs(-3))

# 对于复数而言，abs返回的是复数的摸
# sqrt(1+2*2)
print(abs(1+2j))

#  int 取整函数,截取整数部分
# 520
print(int('520'))
# 9
print(int(9.99))

#  float计算
print(float('3.14'))
print(float('+1E6'))
# 需要注意的是转换的字符串中间不能存在空格
print(complex('1+2j'))



##  幂运算以及幂乘运算
print(pow(2,3))
print(2 **  3)
print(2 **  -3)
#pow(2,3,5)=== 2 **  3 %5  最终的计算结果是3


"""
  函数对应的是一个工厂的，对应的是一个输入和输出组建。
"""


