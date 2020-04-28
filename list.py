#  python中是没有数组的，具有更加强大功能的列表的。
#  创建列表,下面的member对应的是一个列表的
member=['小甲鱼','小布丁','黑夜','迷途','怡静']
for  each in member:
    print(each,len(each))

number=[1,2,3,4,5]
print(number)

mix=[1,'小甲鱼',3.14,[1,2,3]]
print(mix)

# 创建空的列表
empty=[]
# 给列表增加元素,对应的常见的方法
member.append('福禄娃娃')
print(len(member))
# 只能加入一个元素的
member.append('竹林小溪')
# extend的操作对应的是一个列表的,对应的extend操作的是一个列表的，自动追加到列表尾部
member.extend(['crazy迷恋','竹林小溪'])
print(len(member))
#  在第一个位置增加元素牡丹
member.insert(0,'牡丹')
print(member)
#  列表对应的是从0开始的。

#  获取列表的第一个元素
print(member[0])

# 列表的变量替换
temp=member[0]
member[0]=member[1]
member[1]=temp;

print(member[0])
print(member[1])

# 从列表中删除元素或者剔除元素
member.remove('怡静')
print(member)
# 元素不存在的话，对应的会出现异常的
#member.remove('小鱼儿')
##  方式二，使用del语句删除列表元素
del member[0]
#  删除列表  del member
print(member)

# python 中的list对应的采用的是栈的操作方式的，先进后出的方式的。pop弹出
print(member.pop())
name=member.pop()
print(name)
# 弹出指定索引的数据
print(member.pop(1))

# 列表分片和切片操作，使用列表分片可以一次性的获取多个元素
#  1<=a<3 
print(member[1:3])
#  获取从开始到3的元素，不包含3
print(member[:3])
# 获取从1开始的元素。
print(member[1:])
# 进行元素列表的拷贝操作
print(member[:])

# 列表的后续操作
list1=[123]
list2=[234]
# 对应的结果是false
print(list1>list2)
#
list1=[123,456]
list2=[234,123]
# 进行列表元素的比对，第一个元素比较出来结果的话，后续的就不用进行比对了。 False,和字符串的比较是类似的
print(list1>list2)

list3=[123,456]
#  对应的结果为true
print(list1<list2 and list1==list3)
#  元素的拼接在一起的。使用exend进行元素的增加的，更加推荐的。
list4=list1+list2
print(list4)
list4.append(789)
print(list4)
list4.extend([891,123])
print(list4)
#  列表复制元素
print(list1*3)
list1*=3
print(list1)
#  循环的遍历 ，range  
print(123 in list1)
print('小甲鱼' not in member)

# 列表中的元素进行in 以及 not in
list5=[123,['小甲鱼','牡丹'],456]
# in  只能够判断一层的关系的
print('小甲鱼' in list5[1])
# False
print('小甲鱼' in list5)
#True 
print('牡丹' not in list5)
# 访问多层结构
print(list5[1][1])

# dir 获取内置的函数
print(dir(list))


# 厂家的list的方法
# 计算指定的元素在列表中出现的次数
print(list5.count(123))
# 返回参数在列表中出现的位置
print(list5.index(456))
# 指定查找元素的位置的，起始位置
print(list1.index(123,3,7))
#  reverse 进行列表反转
list5.reverse()
print(list5)
# sort排序操作
list6=[4,3,5,1,9,23,32,0]
#  默认的是按照升序的排列方式进行排列的
list6.sort()
print(list6)
# 执行从大到小排序，首先执行sort,然后执行reverse的方法的
list6.sort(reverse=True)
print(list6)
# 执行元素的拷贝操作,重新创建了一份列表元素
list7=list6[:]
print(list7)
# list8对应的还是元素的列表的。
list8=list6
print(list8)
#  执行修改
list6.sort()
print(list7)
print(list8)
# python变量对应的是一个标签的概念的，对应的是指哪打哪的操作的。
# 执行元素的拷贝的话，推荐使用分片的方式进行列表的拷贝操作。






