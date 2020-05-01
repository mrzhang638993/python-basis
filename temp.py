count=0
# 从12个求中选择8个球进行组合操作
for i in range(2,7):
    # 从绿色球中至少可以获得2个球，最多可以获取到6个球
    #  需要判断球的数量。不能够超过3个球
    # 需要循环处理一下
    for j  in range(0,3 if 8-i>=3 else 8-i):
        print(i,j,8-i-j)
        count=count+1
print(count)
