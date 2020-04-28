#  三元表达式的书写  x if 条件 else y 条件成立为x，否则为y
#断言  assert 出现异常的时候给与崩溃的机制的,可以在程序中设置调试点的操作的，很有效的操作的。
#assert 3>4


# 循环操作  while  for 循环
"""
  while 条件：
    循环体
"""
"""
 for 目标  in  表达式：
    循环体
"""
#  循环体的执行和操作
favourite="FishC"
for i in favourite:
    print(i,end=" ")

# len对应的返回字符串的长度
member=['小甲鱼','小布丁','黑夜','迷途','怡静']
for  each in member:
    print(each,len(each))

#  range(start,stop,step=1) 生成start 到 stop之间的，步长为1的列表
print(range(5))
# 生成 0 1 2 3 4
for i in range(5):
    print(i)

# 返回的是一个list
print(list(range(5)))

#  返回数值信息,返回的是2~9之间的数值的，不包含9的数值的。
for k in range(2,9):
    print(k)
#  返回1~9之间的数字的，不包含9，步长为2
for j in range(1,9,2):
    print(j)
# 打印的是2,3两个元素的
for i in (2,3):
    print(i)


#  break 语句和continue 语句
# 下面的循环中的i 是不会随着里面的i的变化而变化的
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    else:
        i +=2
        print(i)

