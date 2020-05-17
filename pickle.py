#  可以将python对象转化成为二进制流，或者是将二进制流转化为对象也是可以的。
#  对象的序列化写入和序列化写出操作，这个很关键
import pickle
my_list=[123,3.14,'小甲鱼',['another list']]
pickle_file=open("my_list.pkl",'wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()

# pkl文件的读取操作
import pickle
pickle_file=open("my_list.pkl",'rb')
my_list=pickle.load(pickle_file)
print(my_list)

#大量复杂的列表的话，可以使用pickle模块进行操作的。
import pickle
f=open('record.txt','rt')
# 下面分段截取出来文本的内容
content=f.read()
list1=content.split("=")
for each in list1:
    if not each=="=":
        print(each)

    



