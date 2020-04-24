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





