x=3  #代码注释
print(x)
loveyou1234=1234
#520baby=420  变量名称不合法
幸运数=588
print(幸运数)


name="小甲鱼"
print(name)
name="老乌龟"
print(name)


x=3
y=5
y=x
print(y)

x=y=3
print(x,y)

x=3  # 执行变量x,y之间的变量交换操作
y=5
temp=y
y=x
x=temp


x=3
y=5
x,y=y,x   #  变量x,y之间的变量交换
print(x,y)


#####下面是字符串的操作
# ‘’单引号的字符串
print('i love china')
# "" 双引号包裹的字符串
print("let's go")
# 显示双引号
print('"life is  short ,you need  python"')
##包含单引号和双引号的，比较复杂的话，推荐使用转义字符,复杂的单引号和双引号之间的交互推荐使用转义字符
print('\"life is  short,let\'s study python')
# 打印换行
print("i love python\ni love fishc.com.cn")


##使用原始字符串，不能跨行的
print("D:\three\two\one\now")
# 需要使用如下的操作才可以输出原来的字符
print("D:\\three\\two\\one\\now")  #对反斜杠的本身进行转义
#可以使用原始的字符串来创建字符串的，避免字符串的转义操作
print(r"D:\three\two\one\now") # r代表的是原始的字符串
#  \ 代表的是没有结束的。可以构建很长的字符串的。
#  长字符串
poetry="""
  面朝大海，春暖花开
  从明天起，做一个幸福的人
  喂马，劈柴，周游世界
  从明天起，关心粮食和蔬菜
  我有一所房子，面朝大海，春暖花开

  从明天起，和每一个亲人通讯
  告诉他们我的幸福
  哪幸福的闪电告诉我的
  我将告诉每一个人

  给每一条河流每一座山取一个温暖的名字
  陌生人，我也为你祝福
  愿你有一个灿烂的前程
  愿你有情人终成眷属
  愿你在尘世获得幸福
  我只愿面朝大海，春暖花开
"""
print(poetry)


#字符串的加法和乘法
520+1314
# 字符串拼接
'520'+'1314'
## 一次性的打印3000遍的字符串
print("我每天爱你三千遍"*300)  # 字符串的乘法

# 字符串的操作
"""
下面的语句报错的原因在于int不能显式的转化为字符串的。
"""
print("i love  fish.com"+str(8))
# 字符串的常见的方法操作
str1='I love fishc.com'
# 切片操作
print(str1[:6])
print(str1[:6]+'插入的字符串'+str1[6:])
str2='DAXIExiaoxie'
print(str2.casefold())  # 对应的进行大小写的转换操作
print(str2.center(40))  # 对应的输出字符串的时候进行居中处理。
print(str2.count('xi'))  # 对应的统计str2当中xi字符串出现的次数
print(str2.endswith("xi"))   # 判断字符串是否是xi结尾的字符串
print(str2.find('efc'))  # 查找字符串中efc是否出现，没有的话反悔-1
#print(str2.index('efc'))      #返回对应的数值信息
#print(str2.istitle())  # 判断字符串是否是标题，标题对应的是大写字母开头的，后面的都是小写字母的。
#print(str2.join('xfc'))  #  字符串中的每一个字符后面填充xfc的字符串。
#print(str2.lower())     # str2中的字符串全部转化为小写字符。
#  split 进行字符串的自动的切割操作

#  字符串的格式化操作，按照统一的格式输出字符串。
#  位置参数格式化输出
"{0} love {1}.{2}".format("i","FishC","com")
#  关键字格式化输出
"{a} love {b}.{c}".format(a="i",b="FishC",c="com")
# 需要注意的是位置参数需要位于关键字参数之前的

"{{0}}".format("不打印")  # 对应的输出的内容为 {0}
'{0:.1f}{1}'.format(27.658,'GB')  # 对应的内容输出为 27.7GB
'%c'  % 97
'%c,%c,%c'  % (97,98,99)
'%s'   % 'i love FishC.com'
'%d + %d = %d'  %(4,5,4+5)
'%o'  % 10
'%x'  % 10
'%X'  % 10
'%X'  % 160
'%f'  % 27.658
'%e'  %  27.658
'%E'  %   27.658
'%g'  %  27.658
'%f'  % 27.658
'%5.1f' % 27.658
'%.2e'  %  27.658
'%10d'  %  5
'%-10d'  % 5
'%+d'    % 5
'%+d'    % -5
'%#o'  % 10
'%#X'   % 108
'%#d'   % 10
'%010d'  % 10
'%-010d'   % 5








