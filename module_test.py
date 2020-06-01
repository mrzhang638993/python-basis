def c2f(cel):
    fah = cel * 1.8 + 32
    return fah


def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel


"""
 对应的实现代码模块的测试和操作实现
"""


def test():
    print("测试0摄氏度等于=%.2f华氏度" % c2f(0))
    print("测试0华氏度等于=%.2f摄氏度" % f2c(0))


test()
