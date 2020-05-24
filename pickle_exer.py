

# pickle程序答案
# pickle 的实质实际上是对象的序列化操作和反序列化的操作的
# 使用pickle的dump方法存储数据
# 使用pickle的load加载数据到内存
# pickle可以将对象的数据保存为任何形式的

"""
编写一个程序，这次要求使用pickle将文件（  record.txt (1.1 KB, 下载次数: 7693) ）里的对话按照以下要求腌制成不同文件（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件（提示：文件中不同的对话间已经使用“==========”分割）
"""
import pickle_1
f=open('record.txt','rt')
# 下面分段截取出来文本的内容
content=f.read()
list1=content.split("=")
count=1
for each in list1:
    if  not each=="" and not each=='\n':  # each对应的是一个字符串的
        list2=each.split("\n")
        f=open('boy_'+str(count)+".txt",'wt')
        f1=open('girl_'+str(count)+".txt",'wt')
        for each1 in list2:
            if not each1=='':
                if not each1.find("小甲鱼:")==-1:
                    f.write(each1.replace("小甲鱼:","")+"\n")
                elif not each.find("小客服:")==-1:
                    f1.write(each1.replace("小客服:","")+"\n")
        f.close()
        f1.close()
        count +=1
