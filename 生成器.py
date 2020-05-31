# 生成器对应的是迭代器的一种实现，所以可以使用迭代器的方式实现迭代操作的
def myGen():
    print("生成器被执行")
    yield 1
    yield 2


myG = myGen()
print(next(myG))
print(next(myG))


# 定义斐波拉切数列
def fibs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a  # 不要丢掉了a，否则下面的会报错的


for each in fibs():
    if each > 100:
        break
    else:
        print(each, end="   ")
# 获取可以被2整除但是不能被3整除的数字
a = [i for i in range(100) if not (i % 2) and (i % 3)]
print(a)
b = {i: i % 2 == 0 for i in range(10)}
print(b)
c = {i for i in [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 3, 2, 1]}
print(c)
#  不会进行迭代的操作的
d = "i for i in 'I love fishc.com'"
print(d)
# 元祖推导式
e = (i for i in range(10))
#  e对应的是生成器的推导式的
print(e)
print(next(e))
for each in e:
    print(each)

# 对应的执行相关的调度操作
total = sum((i for i in range(100) if i % 2))
print(total)
total1 = sum(i for i in range(100) if i % 2)
print(total1)
