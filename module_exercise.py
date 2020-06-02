# python中的模块对应的是一个python文件
"""
1.我们现在有一个 hello.py 的文件，里边有一个 hi() 函数：.&ymiM?t
def hi():
    print("Hi everyone, I love FishC.com!")
复制代码
请问我如何在另外一个源文件 test.py 里边使用 hello.py 的 hi() 函数呢？
答案：对应的引用方式是如下的：
import  hello_1 as hello
hello.hi()
2.模块对应的引入方式主要包括如下的3中引入方式的：
导入方式之一：import 模块导入操作
导入方式之二：from  模块名称 import  函数名称  可以只引入部分的名称
导入方式之三： import  模块名称  as  新名字  推荐使用这个方式来实现操作的
3. 曾经我们讲过有办法阻止 from…import * 导入你的“私隐”属性，你还记得是怎么做的吗？
from  模块名称 import  函数名称 可以避免导入函数的私有属性的。
4. from a import sayHi
from b import sayHi
sayHi()
对应的存在覆盖的问题，执行的是下面的一个函数的操作的
5.出现下面的问题对应的解决的办法是：
# a.py
from b import y
def x():
    print('x')
# b.py
from a import x
def y():

    print('y')
存在对应的循环依赖的办法实现的。
"""
import const

const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)
