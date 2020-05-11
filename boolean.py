

#False  True
print(bool(250))
print(bool("假"))
print(bool("False"))
print(bool(False))
#  空字符串对应的是false
print(bool(""))
# 0对应的是false
print(bool(0))
print(bool(0.0))
# 0对应的是false
print(bool(0j))

"""
出现如下的情况，对应的结果是false
1.定义为False的对象：None False
2. 值为0的数据类型：0,0.0，Decimal(0),Fraction(0,1)
3.空的序列和集合 "" , (),{},set(),range(0)
"""

#  分支和循环语句
if 520>250:
    print("520比250大")
else:
    print("520不比250大")

#可以简化为如下的
if  bool(250):
    print("250 is Ture")
else:
    print("250 is False")

##  boolean对应的其实就是一种特殊的整数类型的数据
print(1==True)
print(True+False)
print(True-False)
print(True*False)
#print(True/False)

##  逻辑运算符 and or  not
print(3<4 and 4<5)
print(3<4 and 4<5)
print(3<4 and 4>5)
print(3>4 and 4>5)

print(3<4 or 4<5)
print(3>4 or 4<5 )
print(3<4 or 4>5)
print(3>4 or 4>5)

#  not操作：获取原来结果相反的boolean数值
print(not  True)
print(not   False)
print(not 250)
print(not 0)

# and 以及 or表达式都是需要进行短路计算的。
#  4 ,and表达式需要计算后面的4作为最终的表达式结果
print(3 and 4)
# 4  ， 逻辑表达式4已经为真，不用继续测试的，4作为最终的结果的
print(4 or 5)
#  and需要执行最后的表达式的，表达式的数值对应的是真值的
print("FishC" and "LOVE")
# 250 
print("FishC" and 250)
#  4 
print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9))
# 4 
print( False or 0 or 4 or 6 or  9)
# 4,对应的存在相关的优先级的，and的优先级高于or。not 的优先级高于and
print(not 1  or 0 and 1 or 3 and 4  or  5 and 6  or 7 and 8 and 9)

#  运算符的优先级


