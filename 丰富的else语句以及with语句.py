try:
    print("abc")
except ValueError as reason:
    print("出错了:"+str(reason))
else:
    print("没有任何异常!")

#  报错的情况下,是不会执行else语句的，只是会执行except语句的。
try:
    number=int(input("请输入数据:"))
except  ValueError as reason:
    print("出错了:",reason)
else:
    print("没有任何异常!")

# with 语句，可以将文件的打开和关闭进行封装，推荐使用with进行文件的操作的
try:
    with open('data.txt','w') as f:  #with语句对应的会执行自动的文件关闭操作的
        for each in f:
            print(each)
except OSError as  reason:
    print("出错了:"+str(reason))
    

