#元祖对应的是内部的元素是不可变的。
# 创建元祖
tuple1=(1,2,3,4,5,6,7,8)
# 2
print(tuple1[1])
#  6 7 8 
print(tuple1[5:])
#  1 2 3 4 5
print(tuple1[:5])
#  进行元祖的拷贝 1 2 3 4 5 6 7 8 
print(tuple1[:])

# 试图修改元祖的元素的话，对应的会报错的
#tuple1[1]=10
# type 可以测试相关的数据类型,区别于元祖的关键在于逗号，而不是小括号的。
temp=(1)
print(type(temp))
temp=2,3,4
print(type(temp))
# 创建空元祖
temp=()
print(type(temp))
# 创建一个元素的元祖
temp=(1,)
print(type(temp))
temp=1,
print(type(temp))


#更新和删除元祖
temp=('小甲鱼','黑夜','迷途','小布丁')
temp=temp[:2]+('怡静',)+temp[2:]
print(temp)
# 使用切片的方式实现元祖中的元素的删除操作的。
# 删除整个的元祖，可以使用del 语句删除的
del temp
# 删除之后，对应的会报错的.
#print(temp)
#  python  对应的回收机制可以进行垃圾回收的。

#  可以作用于元祖的操作符：
# 1.+ ,*,> <  in  not in  and or  可以使用用于元祖的，对应的和list的是差不多的。


