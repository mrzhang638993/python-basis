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
import os
f=open("OpenMe.mp3",'rb')
content=f.read()
f1=open("OpenMe.txt",'w')
f1.write(str(content))
f1.close()
f.close()

