member=['小甲鱼','小布丁','黑夜','迷途','怡静']
print(member)
number=[1,2,3,4,5]
print(number)
mix=[1,'小甲鱼',3.14,[1,2,3]]
print(mix)

# 不知道放置什么元素，但整体对应的是一个列表的，可以使用空的列表
empty=[]
# 向列表中增加元素
# append 对应的是向列表的尾部增加元素
member.append('福禄娃娃')
print(len(member))
# 一次性的增加多个元素,增加到元素的尾部
member.extend(['竹林小溪','Crazy迷恋'])
print(member)
print(len(member))
# 制定位置元素插入操作，指定索引位置插入，默认的是从0开始的。
member.insert(1,'牡丹')
print(member)
# 从列表中获取元素
print(member[0])
print(member[1])
# 元素交换
temp=member[0]
member[0]=member[1]
member[1]=temp
print(member)

#列表元素移除
member.remove('怡静')
print(member)
del member[0]

#  python的列表使用的是pop的栈进行操作的
member.pop()  # 移除列表的尾部元素
name=member.pop() # 移除列表尾部的元素，输出对应的元素值
print(name)
print(member)
member.pop(1)  # 弹出指定位置的元素

# 列表分片，一次性的可以获取多个元素.获取到的是列表的拷贝的，原来的列表收不会发生改变的
print(member[1:3])
member[:3] # 获取从开始到索引为3的元素
member[1:]  # 获取索引值从1开始的元素
member[:]  #  获取到的是列表的拷贝的

# 列表集合的操作
list1=[123]
list2=[234]
print(list1>list2)  # False
list1=[123,456]
list2=[234,123]
print(list1>list2) # 列表比较的话，对应的如果第一个元素可以确定大小的话，后续的就不用比较了。前面的元素可以比较出来结果的话，后面的是不用比较的。
list3=[123,456]
print(list1>list2 and list1==list3)
list4=list1+list2  # 列表的拼接操作的，不推荐使用这种方式实现操作的。
# * 重复操作符
print(list3*3)
list3 *=5
print(list3)

# 成员操作符号： in not in  只能判断一层的元素的关系的，当列表是多层的话，需要制定层次的
print('小甲鱼' not in list3)
list5=[123,['小甲鱼','牡丹'],456]
print('小甲鱼' in list5)
print('小甲鱼' in list5[1])
print(list5[1][1])   #  访问列表的元素
print(list5.count(123))  # 查询元素中指定元素的个数
print(list5.index(123,0,7))  # 查找范围的起始位置
# reverse对应的执行元素的反转操作
list3.reverse()
# sort()对应的进行排序，默认的是从小大的排序操作的
list6=[4,2,5,1,9,23,32,0]
list6.sort()
print(list6)
# 从大到小的排序操作 sort(reverse=True)
list6.sort(reverse=True)  # 降序排列数据
print(list6)
list7=list6[:] # 列表拷贝，对应的是新建了一个新的列表数据的
print(list7)
list8=list6    # 对应的列表是原来的列表的，没有拷贝形成新的数组


# 元祖的学习和操作，元祖对应的是一种不可改变的数据类型.元祖的数据是不能修改的,类似于Java中的String
tuple1=(1,2,3,4,5,6,7,8)
print(tuple1)
print(tuple1[1])
# 下面是元祖的切片操作
print(tuple1[5:])
tuple2=tuple1[:]  # 对应的进行元祖的拷贝操作
print(tuple2)

# 元祖的定义：关键是逗号是元祖的关键的，不是()的
temp=(1)
print(type(temp))   #  int类型的，不是元祖的类型的

temp=(1,)
print(type(temp))  #  tuple元祖操作

# 定义元祖的类型
temp=()
print(type(temp))

# 定义元祖类型
temp2=3,4,5
print(type(temp))  # 对应的是元祖的类型的

8*(8,)  # 复制了8个元祖

# 更新和删除一个元祖进行操作
temp=('小甲鱼','黑夜','迷途','小布丁')
temp2=temp[:2]+('怡静',)+temp[2:]   # 切片创建一个新的元祖
print(temp2)

#删除元祖，包括单个元素以及整个的元素
del  temp2  #删除单个的标签进行操作

# 元祖相关的操作符号，后续的元祖和列表相关的知识需要学习的


















