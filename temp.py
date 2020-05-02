








member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member=member[:1]+[88]+member[1:2]+[90]+member[2:3]+[85]+member[3:4]+[90]+member[4:5]+[88]
#  采用迭代器的方式实现迭代操作
it=iter(member)
for x in it:
    print(x,next(it))
