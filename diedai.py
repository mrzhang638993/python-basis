# -!- coding: utf-8 -!-
"""字符串对应的是迭代器的"""
for i in 'fishC':
    print(i)

links = {
    '鱼c工作室': "http://www.fishc.com", \
    '鱼c论坛': "http://bbs.fishc.com", \
    '鱼c博客': "http://blog.fishc.com", \
    '支持小甲鱼': "http://fishc.taobao.com"
}
# 下面演示的是迭代的操作实现逻辑
for each in links:
    print("%s--->%s" % (each, links[each]))
for i in links.values():
    print(i)
#  python的迭代，2个内置的bif iter，next
string = 'fishC'
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

string = 'FishC'
it = iter(string)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


# 对应的魔法方法，对应的实现下面的方法对应的方法对应的就可以实现对于代码的运用的
#  iter需要实现__iter__ 内置的模仿方法的
#  next 对应的实现了__next__的内置方法的
class Fibs:
    def __init__(self, n=20):  # n 代表的是控制迭代的范围
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        # 执行a,b字符的交换操作
        self.a, self.b = self.b, self.a + self.b
        if self.a >= self.n:
            raise StopIteration;
        else:
            self.n += 1
            return self.a


fibs = Fibs()
for each in fibs:
    try:
        print(each)
    except Exception as reason:
        print(reason)
