#  创建和访问字典
brand=['李宁','耐克','阿迪达斯','鱼C工作室']
slogin=['一切皆有可能','Just do it','Impossible is nothing','让编程改变世界']
print('鱼C工作室的口号是:',slogin[brand.index('鱼C工作室')])
# 字典的标志性的序号是{}
#  创建和访问字典,字典是映射类型,包含key,value
dict1={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing',"鱼C工作室":'让编程改变世界'}
print('鱼C工作室的口号是:',dict1['鱼C工作室'])
dict2={1:'one',2:'two',3:'three'}
print(dict2)
print(dict2[2])
# 创建一个空的字典
dict3={}
help(dict)  # 查询字典的用法和实现逻辑
#  构建字典
dict3=dict((('F',70),('i',105),('s',115),('h',104),('c',67)))
print(dict3)
# 小甲鱼,苍井空 对应的都是key的操作的
dict4=dict(小甲鱼='让编程改变世界',苍井空='让AV征服所有宅男')
print(dict4)
dict4['苍井空']='所有AV从业者都要学习编程提高职业技能'
print(dict4)
dict4['爱迪生']='天才就是99的汗水+1%灵感,但这1%的灵感比99%的汗水更加重要'
print(dict4)
#  python 唯一的映射类型就是字典，dict对应的是一个类型的，dict对应的是工厂函数
dict5={}  # 定义空的字典
dict5=dict5.fromkeys((1,2,3))
print(dict5)
dict5=dict5.fromkeys((1,2,3),'Number')  #  创建的是一个新的字典。
print(dict5)
# 下面是创建的一个新的字典进行的操作的
dict5=dict5.fromkeys((1,3),'数字')
print(dict5)
#  访问字典的几个常见的方法
dict1=dict.fromkeys(range(32),'赞')
print(dict1)
for  eachkey in dict1.keys():
    print(eachkey)  # 打印出来的是dict的key
for eachValue in dict1.values():
    print(eachValue)
# 打印的是字典中的每一个项
for eachItem in dict1.items():
    print(eachItem)
#  字典在key不存在的时候，会对应的报错的
#print(each[32])
print(dict1.get(32)) # 返回的是None的数据的
#  判断对应的key是否存在的，不存在的话，不会报错的
print(32 in  dict1)    #  判断对应的key是否存在的
print(31 in  dict1)
# 对应的执行相关的判断逻辑和实现操作的逻辑
# 清空字典
dict1.clear()
print(dict1)
#
print(dir(dict))
#  下面是浅拷贝相关的赋值操作
a={1:'one',2:'two',3:'three'}
b=a.copy()
c=a
print(id(a))  #浅拷贝的地址
print(id(b))  # 浅拷贝的地址
print(id(c))  # 浅拷贝的地址
# 对应的浅拷贝操作的话，对应的浅拷贝的地址是不一样的。需要进行关注操作和实现。只是对于对象的浅层拷贝的
print(a.pop(2))  #  弹出指定的key对应的键值操作的
print(a.popitem())    #  弹出指定的item,对应的key是随机的，可以随便弹出item的，没有顺序的
#  对应的完成相关的数据设计操作
a.setdefault('小白')   # 没有数值的话，设置为None的操作的
print(a)
a.setdefault(5,'five')  # 设置默认的数值
print(a)     # 字典中没有特定的顺序的
#  update方式更新字典
b={'小白':'狗'}
a.update(b)  # 使用b来更新字典a的数据的
print(a)

#  集合的操作
num={}
print(type(num))  # 对应的是字典类型
num2={1,2,3,4,5}
print(type(num2))  # 对应的是集合的数据set类型的集合数据。没有体现映射关系
#  set对应的数据结构是可以确保数据的唯一特性的
num2={1,2,3,4,5,5,4,3,2}   # 集合中的数据是唯一的，可以确保集合的唯一特性的
# 集合的数据是无序的，是不支持集合的类型和操作的
# 创建序列 set() 工厂方法
set1=set([1,2,3,4,5,5])
print(set1)
#去除列表中的重复的元素
num1=[1,2,3,4,5,5,3,1,0]
temp=[]
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
#  程序关注允许的话，使用set的时候需要进行关注的。
print(1 in  num2)
# 相关的逻辑操作推荐
num2.add(6)
print(num2)
#  元素的移除操作
num2.remove(5)
print(num2)
#不可变集合，定义不可变的集合，不需要进行修改的
num3=frozenset({1,2,3,4,5})
#num3.add(0)    # 对应的增加元素的话，程序会报错的
print(num3)









    






