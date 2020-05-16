##def queryRelationer():
##    name=input("请输入联系人姓名")
##    print(name+":",dict1["phone"])
##def insertRelationer():
##    name=input("请输入联系人姓名")
##    phone=input("请输入联系人电话")
##    dict1.setdefault(name,phone)
##    print(dict1)
##def deleteRelationer():
##    name=input("请输入联系人姓名")
##    dict1.pop(name)
##def exitRelationer():
##    return 0
##print("""
##欢迎进入通讯录程序
##1:查询联系人资料
##2:插入新的联系人
##3:删除已有的联系人
##4:退出通讯录程序
##""")
##dict1={"小甲鱼":"020-88974651"}
##index=int(input("请输入相关指令:"))
##if  index==1:
##    queryRelationer()
##elif index==2:
##    insertRelationer()
##elif index==3:
##    deleteRelationer()
##elif index==4:
##    exitRelationer()
##else:
##    print("输入错误")
#  用户登录程序操作
#定义几个函数实现封装操作
##dict1={"小甲鱼":"FishC"}
##def createUser():
##    name=input("请输入用户名:")
##    if not dict1.get(name)==None:
##        print("您输入的用户名已经存在，请重新输入")
##        name=input("请输入用户名:")
##    password=input("请输入密码")
##    dict1.setdefault(name,password)
##def  userLogin():
##     name=input("请输入用户名:")
##     if dict1.get(name)==None:
##         print("您输入的用户名不存在，请重新输入")
##         name=input("请输入用户名:")
##     password=input("请输入密码")
##     if  dict1.get(name)==password:
##         print("欢迎进入xxoo系统，请点击上角的x结束程序")
##     else:
##          print("密码不正确，拒绝登录")  
##print(""""
##新建用户：N/n
##登录账号: E/e
##退出程序:Q/q
##""")
##index=input("请输入指令代码:")
##if index=='N' or index=='n':
##    createUser()
##elif index=='E'  or index=='e':
##    userLogin()
##elif index=='Q'  or index=='q':
##    exit 
##else:
##    print("系统输入的不正确，请重新输入操作")
#  创建一个不变元素的集合
##set1=frozenset({1,2,3,4,5})
##print(set1)
##print(len(set1))
###set1 = {[1, 2]}
##set1 = set([1, 2])
##import pickle
##my_list=[123,3.14,'小甲鱼',['another list']]
##pickle_file=open('my_list.pki','wb')
##pickle.dump(my_list,pickle_file)
##pickle_file.close()
##import pickle
##pickle_file=open('my_list.pki','rb')
##my_list2=pickle.load(pickle_file)
##pickle_file.close()
##print(my_list2)
##import os
##try:
##     f=open('我为什么是一个文件.txt','a')
##     print(f.write('我存在了吗'))
##     i=1+'1'
##except OSError as  reason:
##    print(reason)
##finally:
##     f.close()
##try:
##     with open('我为什么是一个文件.txt') as f:   #  with 语句会关注文件的状态的，对应的调用f.close的相关的方法的。
##         print(f.write('我存在了'))
##         i=1+'1'
##         f.close()
##except  OSError as  reason:
##    print("出错了",reason)
##import pickle
##my_list=[123,3.14,'小甲鱼',['another list']]
##pickle_file=open('good.pki','wb')
##pickle.dump(my_list,pickle_file)
##pickle_file.close()
##import pickle
##pickle_file=open("good.pki",'rb')
##my_list2=pickle.load(pickle_file)
##pickle_file.close()
##print(my_list2)
##import os
##f=open("good.txt",'r',encoding='utf-8')
##print(f.read(10))  #  获取文件指针的位置操作
##print(f.tell())
##f.close()
##import os
##f=open("OpenMe.mp3",'rb')
##print(f.read())
##f.close()
##import os
##f=open("OpenMe.mp3",'rb')
##content=f.read()
##f1=open("OpenMe.txt",'w')
##f1.write(str(content))
##f1.close()
##f.close()
##import os 
##str1 =''
##fileName=input("请输入文件名:")
##print("请输入内容[【单独输入':w'保存退出】:")
###下面开始一行行的输入文件的内容，输入 :w 进行判断操作
##for line in iter(input,':w'):
##    str1+=line+"\r\n"
##f=open(fileName,'w')
##f.write(str1)
##f.close()
##import os
##fileName1=input("请输入需要比较的头一个文件名:")
##fileName2=input("请输入需要比较的另一个文件名:")
##f1=open(fileName1,'r')
##f2=open(fileName2,'r')
###  比较的是同样的一行数据的,对应的是你读取一行，我读取一行数据的
##count=0
##while 1:
##    count +=1
##    line1=f1.readline()
##    line2=f2.readline()
##    if not line1 and not  line2:
##        break
##    else:
##        if not line1==line2:
##            print("第",count,"不一样")
##import os
##fileName=input("请输入需要打开的文件:")
##n=input("请输入需要显示的行数:")
##list1=n.split(":")
##start=int(list1[0])
##end=int(list1[1])
##print("文件",os.getcwd(),"的前",n,"的内容如下:")
##f=open(fileName,'r')
##count=0
##str1=""
##while 1:
##    count +=1
##    if count>start and count< end:
##        str1 +=f.readline()
##    else:
##        str2=f.readline()
##        #行尾结束符号
##        if not str2:
##            break   # 行情结尾符号
##print(str1)
##import os
##fileName=input("请输入文件名:")
##ch=input("请输入需要替换的单词或者是字符:")
##ch1=input("请输入新的单词或字符")
##count=0  #  需要统计替换的次数操作
##f=open(fileName,'r')
###  一次性的查找存在的个数
###  可以进行一行行的替换操作的
##content=f.read()
##count=content.count(ch,0,-1)
##print("文件",fileName,"中共有",count,"个",ch)
##print("您确定需要将所有的",ch,"替换为",ch1,"吗?")
##choice=input("【YES/NO】:")
##if bool(choice):
##    content=content.replace(ch,ch1,count)
##f.close()
##with open(fileName,"w") as f2:
##    f2.write(content)
##import os
### 查找当前目录下面各种文件的数目，对应的类似的是一个自己字典的操作的
##result={}   # 定义空字典
##for each in  os.listdir(os.getcwd()):
##    #  获取文件的后缀名称,查找指定的后缀，判断是文件而不是目录的话才可以执行操作。需要判断对应的是文件还是文件夹的操作的
##    if  not each.find(".",0,-1) ==-1:
##        suffix=each.split(".")[1]
##        if result.get(suffix)==None:
##            result[suffix]=1
##        else:
##            result[suffix] +=1
##for each in result.keys():
##    print("改文件夹下面共有类型为【.",each,"】的文件",result[each],"个")
##import os
### 查找当前目录下面各种文件的数目，对应的类似的是一个自己字典的操作的
##result={}   # 定义空字典
##for each in  os.listdir(os.getcwd()):
##    #  获取文件的后缀名称,查找指定的后缀，判断是文件而不是目录的话才可以执行操作。需要判断对应的是文件还是文件夹的操作的
##    if  not each.find(".",0,-1) ==-1 and not each==".git":
##        #  判断文件的大小操作和实现 getsize()
##        print(os.path.basename(each),"【",os.path.getsize(each),"bytes】")
# 这个是只有两层的遍历的，多层的话，对应的需要采用函数递归的方式进行的
##import os 
##path=input("请输入带查找的目录:")
##fileName=input("请输入待查找的目标文件:")
##for each in os.listdir(path):
##    if os.path.isfile(each):
##        if each==fileName:
##            print(os.path.abspath(each))
##    else:
##        if os.path.isdir(each):
##            for each1 in os.listdir(each):
##                if os.path.isfile(each1) and each1==fileName:
##                    print(os.path.abspath(each)+"\\"+each1);
##
##def findFile(path,fileName):
##    if os.path.isfile(path) and path==fileName:
##           print(os.path.abspath(path))
##    else:
##        for each in os.listdir(path):
##            if os.path.isfile(os.path.join(path,each)):
##                 if each==fileName:
##                     print(os.path.abspath(path+"\\"+each))
##            else:
##                 findFile(os.path.join(path,each),fileName)   # 存在问题
##findFile(path,fileName)
##import os
##path=input("请输入待查找的初始目录:")
### 创建一个列表存放带查找的视频格式
##style=['mp4','rmvb','avi']
###遍历所有的文件，将找到的文件内容全部的增加到文件中
##f=open("vedioList.txt","w");
##def findAvFile(path,style):
##    content=""
##    if os.path.isfile(path):
##        for sty in  style:
##            if path.endswith(sty):
##                content +=path
##                content+="\n"
##                f.write(content)
##    else:
##        for each in os.listdir(path):
##            if os.path.isfile(each):
##                for sty in  style:
##                    if each.endswith(sty):
##                        content+=path+"\\"+each
##                        content+="\n"
##                        f.write(content)
##            else:  # 对应的是目录，需要进行目录的操作
##                findAvFile(os.path.join(path,each),style)
##findAvFile(path,style)
##f.close()
import os
path=input("请输入待查找的初始目录:")
content=input("请输入关键字:")
def findContentInfile(path,content):
    position=[]
    if os.path.isfile(path):
        for num,val in enumerate( open(path,'rt',encoding="UTF-8") ):
            contents=val
            if not contents.find(content)==-1:
                print("在文件【",path,"】中找到关键字【",content,"】")
            while not contents.find(content)==-1:
               position.append(contents.index(content))
               contents=contents.replace(content,"",1)
            if  len(position):
                 print("关键字出现在第",num,"行","【",position,"】","个位置")
    else:
        for each in os.listdir(path):
            if os.path.isfile(each):
                for num,val in enumerate( open(path+"\\"+each,'rt',encoding="UTF-8") ):
                    contents=val
                    if not contents.find(content)==-1:
                        print("在文件【",path,"】中找到关键字【",content,"】")
                    while not contents.find(content)==-1:
                       position.append(contents.index(content))
                       contents=contents.replace(content,"",1)
                    if len(position):
                       print("关键字出现在第",num,"行","【",position,"】","个位置")
            else:  # 对应的是目录，需要进行目录的操作
                findContentInfile(os.path.join(path,each),content)
findContentInfile(path,content)

