#  函数,对象，模块操作
def  MyfirstFunction():
    print("这是我创建的第一个函数")
    print("我表示很激动")
    print("在此，我要感谢TVB,感谢CCAV，感谢小甲鱼，感谢各位鱼油")

MyfirstFunction()   # 函数调用的过程，函数对应的查找是从上往下查找操作的。必须先定义然后才可以调用的。
# 函数的作用，主要的目标是首先重复代码的封装操作。
def MySecondFunction(name):
    print(name+'我爱你')
    
MySecondFunction('小甲鱼')
MySecondFunction('小鱿鱼')

# 定义一个新的函数
def  add(num1,num2):
    result=num1+num2
    print(result)
add(1,2)

# 函数的参数的格式一般的3~4的样子就差不多了。
# 函数返回
def add2(num1,num2):
    return num1+num2
print(add2(1,2))

#关键字参数，可以确保函数的参数匹配的。
def SaySome(name,words):
    print(name+"->"+words)
#下面是关键字参数的使用，参数特别多的情况下，这种优势特别的明显的
SaySome(words='让编程改变世界',name='小甲鱼')
#  默认参数：定义的时候给与默认值的参数、下面对应的是默认值参数的，在参数定义的时候给与默认值的
def  SaySome(words="让编程改变世界",name="小甲鱼"):
     print(name+"->"+words)
SaySome()

# 默认参数,调用的时候给与默认的数值进行操作的，增强代码的健壮性。
#关键字参数，函数调用的时候给与的，防止名称对应的赋值错误。
# 可变参数
def test(*params):
    print("参数的长度是:",len(params))
    print("第二个参数是:",params[1])
test(1,'小甲鱼',3.14,5)

#下面还有如下的操作的，下面的params对应的称之为默认参数
def   test1(*params,exp):
    print("参数的长度是:",len(params),exp)
    print("第二个参数是:",params[1])
test1(1,'小甲鱼',3.14,5,exp=6)
#  函数和过程的区别:函数是由返回值的，过程是简单的，特殊的没有返回值的。python对应的是函数的。
def  hello():
    print("hello c")
temp=hello()
print(temp)   #None  是有返回值的。python的所有函数都是有返回值的。

# python动态的确定类型，赋值操作的时候编译器确定类型的。
#  python 可以返回多个数值的
def back():
    return [1,'小甲鱼',3.14]
print(back())
def  back():    # 返回的是一个元祖
    return 1,'小甲鱼',3.14
print(back())

# 函数变量的作用域问题
#  局部变量和全局变量
#  局部变量和全局变量
#  下面的操作对应的是无法修改全局变量old_price的数值的。
def  discounts(price,rate):
    final_price=price*price
    old_price=88  # 试图修改全部变量，内部的话函数会创建一个局部变量的，名称虽然和原来的是一样的。
    print("修改pld_price的值是:",old_price)
    return final_price
old_price=float(input("请输入原价"))  # 全部变量的使用需要尤其关注和小心
rate=float(input("请输入折扣率"))
new_price=discounts(old_price,rate)
print("修改后old_price的值是:",old_price)
print("打折后的价格是:",new_price)

# 在函数内存修改全部变量的数值的话，python会采用屏蔽(shadowling)的机制(创建同名的局部变量）来保护对应的全局变量的
#  下面修改全局变量的值操作
count=5
def  Myfun():
    global count
    count=10
    print(count)
Myfun()
print(count)
# 下面是函数的嵌套,函数的嵌套调用和使用。内部函数的作用域仅存在于外部函数的范围之内的
def fun1():
    print("fun1()正在被调用")
    def fun2():
        print("fun2()正在被调用")
    fun2()
fun1()

#  闭包：函数式编程中常见的编程范式。不同的语言实现闭包的方式不同的
def Fun(X):
    def FunY(y):   #Funy对应的是一个闭包,是一个内部函数的，不能被外部函数访问的。
        return x*y
    return FunY
i=Fun(8)(5)
# 下面是闭包使用全部变量
def Fun1():
    x=5
    def Fun2():
        x*=x   # 调用会存在错误的，不能引用外部的全局变量x，内部会自动的创建局部变量x，没有赋值的
        return x
    return Fun2()
Fun1()
# 下面对应的可以如下的改造的。容器的数据不是存在于栈中的数据的，可以使用容器改造
def Fun1():
    x=[5]
    def Fun2():
        x[0]*=x[0]   # 调用会存在错误的，不能引用外部的全局变量x，内部会自动的创建局部变量x，没有赋值的
        return x[0]
    return Fun2()
Fun1()
# 还可以使用如下的方实现操作的，使用nonLocal的方式实现操作的.实现函数的局部变量的
def Fun1():
    x=5
    def Fun2():
        nonlocal x
        x*=x   # 调用会存在错误的，不能引用外部的全局变量x，内部会自动的创建局部变量x，没有赋值的
        return x
    return Fun2()
Fun1()
#lamada表达式的学习和理解操作，使用lamada表达式创建匿名函数进行操作
def ds(x):
    return 2*x+1
# 下面使用lamada表达式进行函数编程
g=lambda x:2*x+1   # lamaba 表达式语句，返回的是一个函数对象的。
g(5)  # 使用匿名函数操作
def add(x,y):
    return x+y
add(3,4)
t=lambda x,y:x+y
t(7,8)
#  常见的内置函数的使用,filter对应的实现过滤的操作
filter(None,[1,0,False,True]) # 第一个参数对应的实现的是过滤函数的功能实现的，具体的对应的是函数的过滤器的实现的
list(filter(None,[1,0,False,True]))
# 下面对应的是实现相关的函数过滤的操作实例
#过滤奇数
def  odd(x):
    return x%2
temp=range(10)
show=filter(odd,temp)  #第一个参数对应的是实现处理的函数，第二个参数对应的是数据源。最终获取到的是满足条件的Tue的表达式的
#  转化为一行代码进行实现
list1=list((filter(lambda x:x%2!=0,range(10)))) # 或者是list((filter(lambda x:x%2,range(10))))  默认的1是Tue是可以满足要求的
print(list1)
# map 映射，一个是函数，一个是待处理的数据源的
result=list(map(lambda x:x*2,range(10)))
print(result)
#  递归，不同的程序员使用迭代，天才程序员使用递归函数的
#  使用算法，汉罗塔结构，递归方式实现定义递归体，谢尔宾斯基三角形
#  递归对应的是韩式调用自身的过程的。
def recursion():
    return recursion()
#recursion()  # 对应的存在死循环的操作的。python对应的可以设置递归的深度的操作的。
#  递归的本质是循环的，需要注意循环的控制条件的体现的。初始变量，循环变量的控制，循环变量的判断
def jiechen(x):
    if x==1:
        return x
    else:
        return x*jiechen(x-1)
jiechen(5)
#下面的是非递归版本的。阶乘的话，完全没有必要时用递归的。不建议使用递归完成阶乘的操作的
def  jiechen1(x):
    sum=1
    for i  in range(1,x+1):
        sum = sum*i
    return sum
print(jiechen1(6))
#  斐波那锲数列，迭代和递归实现的版本。不建议使用递归完成菲波那切数列的问题的
def feibonaqie(n):
   n1=1
   n2=1
   n3=1
   if n<0:
       print("输入有误!")
       return  -1
   while n-2>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n -=1
   return n3
result=feibonaqie(20)
if result!=-1:
    print("总共有%d的兔子生成" % result)
# 递归版本的操作
def feibonaqie(n):
    if n==1 or n==2:
        return 1
    else:
        return feibonaqie(n-1)+feibonaqie(n-2)
        


        













