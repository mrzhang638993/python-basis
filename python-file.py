# python 相关的文件的处理操作，需要随机保存数据可以避免数据损失的
#  直接读取文件  for i in file:  比较的推荐的，效率比较的高
# 文件读取和文件系统的相关的操作和实践管理操作的。文件系统相关的学习和实践操作管理实践
#  模块的管理和操作
import  random
secret=random.randint(1,10)
print(secret)
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名称是.py。模块可以被别的程序引入，以使用该模块中的函数等的功能
#  os:操作系统模块，使用了os模块，我们不需要关心什么操作系统下使用什么模块，os模块会帮助我们选择正确的模块进行调用
import os
workdir=os.getcwd();
print(workdir)
os.chdir("D:\\")
print(os.getcwd())
print(os.listdir("E:\\"))
print(os.mkdir("E:\\A"))
print(os.mkdir("E:\\A\\B"))
#print(os.mkdir("E:\\C\\B"))
# 递归创建多层目录
print(os.mkdirs("E:\\C\\B"))
# 文件目录下面的文件为空的时候，才可以删除文件的
print(os.remove("E:\\A\\B\\test.txt"))
print(os.rmdir("E:\\A\\B"))
# os.path模块
# 下面是pickle 模块的使用
# 写文件
import pickle_1
my_list=[123,3.14,'小甲鱼',['another list']]
pickle_file=open('my_list.pki','wb')
pickle_1.dump(my_list, pickle_file)
pickle_file.close()
# 读取文件
pickle_file=open('my_list.pki','rb')
my_list2=pickle_1.load(pickle_file)
pickle_file.close()


