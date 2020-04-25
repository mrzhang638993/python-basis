import decimal
import random
# 6/2 对应的是3.0  是浮点数的
#  浮点数存储的形式不同
#  浮点数的存储对应的存在精度的问题的
#  不是，浮点数的相等需要使用到decimal进行
314000.0
print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3'));

# 硬币的投掷试验
i=0
while i<200:
    result=random.randint(0, 1)
    if result==1:
        print("正面",end="\t")
    else:
        print("反面",end="\t")
    i=i+1

