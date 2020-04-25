import random 
# 对
#  inport  random
#  会
#  返回字符串中的单个的随机字符
print(random.choice("ilovefishc"))
# 下面的两个sed对用的都是一样的
random.seed(1)
print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))
random.seed(1)
print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))
#获取0~99之间的偶数
print(random.randrange(0, 99,2))
# 双色球开奖模拟程序
first=random.randint(1,33)
second=random.randint(1,33)
third=random.randint(1,33)
forth=random.randint(1,33)
fifth=random.randint(1,33)
sixth=random.randint(1,33)
seventh=random.randint(1,16)
print("开奖结果是: ",first,second,third,forth,fifth,sixth)
print("特别号码是: ",seventh)
