"""测试和使用timeit的相关的知识和推荐操作实现"""
import  timeit
# 显示的是timeit的帮助文档操作理念的
print(timeit.__doc__)
# 显示的是timeit定义的方法和类信息的，涉及到具体的使用操作和实现的。
print(dir(timeit))
# 对应的是程序的设计者希望外部可以看到和调用的类信息的。
print(timeit.__all__)
# 对应的是该模块的源代码属性信息,对应的是源代码的位置
print(timeit.__file__)
# 查看相关的模块的帮助文件
print(help(timeit))
#  from  timeit  import * 导入的是all属性中的所有的函数信息的，
#  其他的是无法导入的,对应的是对外暴露的所有的方法和属性信息的
from timeit import *
print(timeit)
print(Timer)
# 快速的提高代码的技巧：
"""
1.不断的代码的编写
2.阅读其他人的代码
3.
"""
