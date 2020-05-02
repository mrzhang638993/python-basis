"""
 主要解决的是元祖,列表以及序列的问题
"""
# 列表中的元素是不做任何的限制的
#  向列表中增加元素可以采用 append 以及insert,extend 方式进行操作
# append 增加的是单个元素，extend()对应的增加的是单个的列表
#  不一样，前面一个报错，后面的可以
name = ['F', 'i', 'h', 'C']
name.insert(2,'s')
print(name)

"""
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
要求将列表修改为：
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
方法一：使用 insert() 和 append() 方法修改列表。
方法二：重新创建一个同名字的列表覆盖。
"""
"""下面是方法一的使用"""
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
print(member)
"""下面是方法二的组合"""
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member=member[:1]+[88]+member[1:2]+[90]+member[2:3]+[85]+member[3:4]+[90]+member[4:5]+[88]
print(member)
for  each in member:
    print(each)
"""修改输出的样式 ['小甲鱼'，88]"""
#实现方式一:
for v,w in zip(member[0:len(member)-1:2],member[1:len(member):2]):
    print(v,w)
# 实现方式二：
#  采用迭代器的方式实现迭代操作
it=iter(member)
for x in it:
    print(x,next(it))
    
#  297
# list1[0] 和 list1[0:1]  是一样的


    


