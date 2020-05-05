# f = open('E:\test.txt', 'w')   # B  对应的存在错误
# 'r' 以只读方式打开文件（默认） 打开文本文件
# open('E:\\Test.bin', 'xb')  对应的是二进制文件形式打开文件
# 因为文件还在使用，对应的文件内容存在于换冲区的，不执行close的话，内容无法写入到文件中


# 写文件
import pickle
my_list=[123,3.14,'小甲鱼',['another list']]
pickle_file=open('good.pki','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
#  下面是将文件报错到列表中
import pickle
mylist2=[]
pickle_file=open("good.pki",'rb',encoding='utf-8')
my_list2=pickle.load(pickle_file)
pickle_file.close()
print(mylist2)
#  迭代文件中的每一行数据
import os
f=open("good.txt",'r',encoding='utf-8')
for each in f.readlines():
    print(each)
f.close()
# 或者是下面的语句
import os
f=open("good.txt",'r',encoding='utf-8')
for each in f:
    print(each)
f.close()
#  下面的语句是读取10个字符
import os
f=open("good.txt",'r',encoding='utf-8')
print(f.read(10))  #  获取文件指针的位置操作
print(f.tell())    #  获取当前文件指针的位置
f.close()
#  python 文件下载
import os
f=open("OpenMe.mp3",'rb')
print(f.read())
f.close()
# 读取文件保存为新的文件
import os
f=open("OpenMe.mp3",'rb')
conent=f.read()
f1=open("OpenMe.txt",'w')
f1.write(content)
f1.close()
f.close()


