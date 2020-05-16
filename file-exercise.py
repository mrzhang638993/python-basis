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
#  文件的相关的操作和实践
"""
从明天起，做一个幸福的人
喂马、劈柴、周游列国 
从明天起，关心粮食和蔬菜 
我有一所房子，面朝大海，春暖花开 

从明天起，和每一个亲人通讯 
告诉他们我们的幸福  
那幸福的闪电告诉我的   
我将告诉每一个人   

给每一条河每一座山去一个温暖的名字  
陌生人，我也为你祝福   
愿你有一个灿烂的前程    
愿你有情人终成眷属           
愿你在尘世获得幸福
我只愿面朝大海，春暖花开   

:w
"""
import os 
str1 =''
fileName=input("请输入文件名:")
print("请输入内容[【单独输入':w'保存退出】:")
#下面开始一行行的输入文件的内容，输入 :w 进行判断操作
for line in iter(input,':w'):
    str1+=line+"\r\n"
f=open(fileName,'w')
f.write(str1)
f.close()

# 输入两个文件比较文件的不同
import os
fileName1=input("请输入需要比较的头一个文件名:")
fileName2=input("请输入需要比较的另一个文件名:")
f1=open(fileName1,'r')
f2=open(fileName2,'r')
#  比较的是同样的一行数据的,对应的是你读取一行，我读取一行数据的
count=0
while 1:
    count +=1
    line1=f1.readline()
    line2=f2.readline()
    if not line1 and not  line2:
        break
    else:
        if not line1==line2:
            print("第",count,"不一样")
f1.close()
f2.close()
# 输出文件的前n行数据
import os
fileName=input("请输入需要打开的文件:")
n=int(input("请输入需要显示该文件的前面多少行:"))
print("文件",os.getcwd(),"的前",n,"的内容如下:")
f=open(fileName,'r')
count=0
while count<n:
    print(f.readline())
    count +=1
f.close()
#  输入指定行数的内容，指定的是时间间隔的操作的
import os
fileName=input("请输入需要打开的文件:")
n=input("请输入需要显示的行数:")
list1=n.split(":")
start=int(list1[0])
end=int(list1[1])
print("文件",os.getcwd(),"的前",n,"的内容如下:")
f=open(fileName,'r')
count=0
str1=""
while 1:
    count +=1
    if count>start and count< end:
        str1 +=f.readline()
    else:
        str2=f.readline()
        #行尾结束符号
        if not str2:
            break   # 行情结尾符号
f.close()
print(str1)

#下面的操作,实现的是全量替换的操作功能
import os
fileName=input("请输入文件名:")
ch=input("请输入需要替换的单词或者是字符:")
ch1=input("请输入新的单词或字符")
count=0  #  需要统计替换的次数操作
f=open(fileName,'r')
#  一次性的查找存在的个数
#  可以进行一行行的替换操作的
content=f.read()
count=content.count(ch,0,-1)
print("文件",fileName,"中共有",count,"个",ch)
print("您确定需要将所有的",ch,"替换为",ch1,"吗?")
choice=input("【YES/NO】:")
if bool(choice):
    content=content.replace(ch,ch1,count)
f.close()
with open(fileName,"w") as f2:
    f2.write(content)

# 下面是文件系统的题目
# 统计当前文件夹下面每一个文件类型的文件数
import os
# 查找当前目录下面各种文件的数目，对应的类似的是一个自己字典的操作的
result={}   # 定义空字典
for each in  os.listdir(os.getcwd()):
    #  获取文件的后缀名称,查找指定的后缀，判断是文件而不是目录的话才可以执行操作。需要判断对应的是文件还是文件夹的操作的
    if  not each.find(".",0,-1) ==-1:
        suffix=each.split(".")[1]
        if result.get(suffix)==None:
            result[suffix]=1
        else:
            result[suffix] +=1
for each in result.keys():
    print("改文件夹下面共有类型为【.",each,"】的文件",result[each],"个")

#编写程序计算文件夹下面文件的大小
import os
# 查找当前目录下面各种文件的数目，对应的类似的是一个自己字典的操作的
result={}   # 定义空字典
for each in  os.listdir(os.getcwd()):
    #  获取文件的后缀名称,查找指定的后缀，判断是文件而不是目录的话才可以执行操作。需要判断对应的是文件还是文件夹的操作的
    if  not each.find(".",0,-1) ==-1 and not each==".git":
        #  判断文件的大小操作和实现 getsize()
        print(os.path.basename(each),"【",os.path.getsize(each),"bytes】")

"""
编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图
"""
import os 
path=input("请输入带查找的目录:")
fileName=input("请输入待查找的目标文件:")
def findFile(path,fileName):
    if os.path.isfile(path) and path==fileName:
           print(os.path.abspath(path))
    else:
        for each in os.listdir(path):
            if os.path.isfile(os.path.join(path,each)):
                 if each==fileName:
                     print(os.path.abspath(path+"\\"+each))
            else:
                 findFile(os.path.join(path,each),fileName)   # 存在问题
findFile(path,fileName)

#
"""
 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，程序实现如图
"""
import os
path=input("请输入待查找的初始目录:")
# 创建一个列表存放带查找的视频格式
style=['mp4','rmvb','avi']
#遍历所有的文件，将找到的文件内容全部的增加到文件中
f=open("vedioList.txt","w");
def findAvFile(path,style):
    content=""
    if os.path.isfile(path):
        for sty in  style:
            if path.endswith(sty):
                content +=path
                content+="\n"
                f.write(content)
    else:
        for each in os.listdir(path):
            if os.path.isfile(each):
                for sty in  style:
                    if each.endswith(sty):
                        content+=path+"\\"+each
                        content+="\n"
                        f.write(content)
            else:  # 对应的是目录，需要进行目录的操作
                findAvFile(os.path.join(path,each),style)
findAvFile(path,style)
f.close()

"""
编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）

对于文件内容的检索和判断
"""
import os
path=input("请输入待查找的初始目录:")
content=input("请输入关键字:")
def findContentInfile(path,content):
    if os.path.isfile(path):
        for num,val in enumerate(open(path,'rt')):
            contents=val
            position=[]
            if not contents.find(content)==-1:
                print("在文件【",path,"】中找到关键字【",content,"】")
            while not contents.find(content)==-1:
               position.add(contents.index(content))
               contents=contents.replace(content,"",1)
            if  len(position):
                 print("关键字出现在第",num,"行","【",position,"】","个位置")
    else:
        for each in os.listdir(path):
            if os.path.isfile(each):
                for num,val in enumerate(open(path+"\\"+each,'rt')):
                    contents=val
                    position=[]
                    if not contents.find(content)==-1:
                        print("在文件【",path,"】中找到关键字【",content,"】")
                    while not contents.find(content)==-1:
                       position.add(contents.index(content))
                       contents=contents.replace(content,"",1)
                    if len(position):
                       print("关键字出现在第",num,"行","【",position,"】","个位置")
            else:  # 对应的是目录，需要进行目录的操作
                findContentInfile(os.path.join(path,each),content)
findContentInfile(path,content)


        
                



    
        




        
        
        
    




        
    



    

    
        

    



