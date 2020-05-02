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

"""
>>> old = [1, 2, 3, 4, 5]
>>> new = old
>>> old = [6]
>>> print(new)
"""
# 输出结果为1 2  3 4 5
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
list2=[]
for x in range(0,10,2):
    for y in range(1,10,2):
        list2.append(x,y)
print(list2)
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0]='小鱿鱼'
print(list1)
# 可以使用sort排序的
list2=[1,8,32,24,96,86]
list2.sort()
print(list2)
# 对列表进行逆序排序
list2.sort(reverse=True)
print(list2)
# 获取是采用如下的方式
list2.reverse()
print(list2)
list3=list2.copy()  # 进行元素的拷贝
print(list3)
list3.clear()  # 进行元素的清空操作
print(list3)
# 列表推导式
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
list2=[]
for x in range(0,10,2):
    for y in range(1,10,2):
        list2.append((x,y))
print(list2)
# 下面是列表推导式的灵活运用
list1=['1.Just do It','2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
list2=['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3=[(y[:]+":"+x[2:]) for x in list1 for y in list2 if x[:1]==y[:1]]
for  each in list3:
    print(each)

#  元素内部是同种类型的，且元素不能变化的情况下使用元祖，其他的使用列表
#   x, y, z = 1, 2, 3  z,y,z不是元祖
#  元祖推导式
list1 = ((x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0)
print(list1)
print(list(list1))  # 对应的是生成的元祖的


# 定义一个跨越多行的str
# 定义方式之一：
str1="""
  goodmorning
  helloworld
"""
print(str1)
#定义方式之二:
str2="goodmoring\
hello world"
print(str2)
#定义方式之三:使用小括号
str3=("  "
     " goodmorning"
      "hellokitty"
      )
print(str3)
# """""" 主要可以使用来进行代码说明
file1 = open(r'E:\works\python-study\flight.txt', 'r') 
# 从指定的url中提取出来对应的字符串，很适合进行爬虫抓取
# 'www.fishc.com'
str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
list1=str1.partition('www.fishc.com')
print(list1[1])
# 下面是有那个负数进行索引值分片操作
print(list1[-2:-1])   # 切割出来的是一个元祖 ('www.fishc.com',)
# 字符串的还原操作
"""
据说只有智商高于150的鱼油才能解开这个字符串（还原为有意义的字符串）：str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
"""
str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])
"""
密码安全性检查的脚本
"""
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0) :
    passwd = input("您输入的密码为空（或空格），请重新输入：")
    length = len(passwd)

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0

# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break
   
# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break   

# 打印结果
while 1 :
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1 :
        print("低")
    elif flag_len == 3 and flag_con == 3 and (passwd[0] in chars):
        print("高")
        print("请继续保持")
        break
    else:
        print("中")

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break

#
"{{1}}".format("不打印", "打印")  # 输出结果为'{1}'
"{a} love {b}.{c}".format(a="I", b="FishC", c="com") # a,b,c对应的是关键字参数
"{0} love {1}.{2}".format("I", "FishC", "com")  # 0,1,2对应的是位置参数
'{0}{1:.2f}'.format('Pi = ', 3.1415)
#进制转换函数脚本
number=input("请输入一个整数(输入Q结束程序):")
if number.isdigit():  #  input输入的话，对应的使用是字符串的，需要进行处理
    dest=int(number)
    print("十进制->十六进制  : ","%#x" % dest)
    print("十进制->八进制  : ","%#o" % dest)
    print("十进制->二进制  : ",bin(dest))
else:
    print("输入错误，请重新输入")
    number=input("请输入一个整数(输入Q结束程序):")

                
        
    




