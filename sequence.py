#  字符串，元祖，列表统一的称之为序列的。
help(list)  #获取内置函数list的帮助文档
str='goodmorning'
str=tuple(str)
print(str)
"""
下面对应的是序列的相关的操作和实现管理
"""
#将元素转化为列表
a=list()   # 生成一个空的列表
b='i love FishC.com'
b=list(b)   # 将字符串转化为一个列表
print(b)
# 元祖
c=(1,1,2,3,5,8,13,21,34)
c=list(c)
print(c)
# 内置函数  tuple，将元素转化为元祖
str1='goodmorning'
str1=tuple(str1)
print(str1)

#  str ,将参数转化为对象
#  len(sub)  返回sub的长度
#  max()   返回参数或者是序列中的最大值
print(max(1,2,3,4,5))
print(max(str1))
#  min 返回序列中的最小值
numbers=[1,18,13,0,-98,34,54,76,32]
print(max(numbers))
print(min(numbers))
chars='1234567890'
print(min(chars))
tuple1=(1,2,3,4,5,6,7,8,9)
print(max(tuple1))
#numbers.append('a')
#  比较的时候，不能将字符串a转化为数字的
print(numbers)
#  sum(str)  返回序列的综合
tuple2=(3.1,2.3,3.4)
print(sum(tuple2))
print(sum(numbers,8))  # 将8加入到sum的总和中
#  sorted()
sorted(numbers)   #对numbers进行排序
reversed(numbers)
list(reversed(numbers))   # numbers反转之后对应的转化成为列表
# 枚举
print(enumerate(numbers))  # 返回numberss的迭代器
print(list(enumerate(numbers)))   # 转哈为列表 [(0, 1), (1, 18), (2, 13), (3, 0), (4, -98), (5, 34), (6, 54), (7, 76), (8, 32)]
a=(1,2,3,4,5,6,7,8)
b=[4,5,6,7,8]
zip(a,b)   # 打包合成元祖 [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
print(list(zip(a,b)))
