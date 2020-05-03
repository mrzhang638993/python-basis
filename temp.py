name=input("请输入带查找的用户名:")
score=[['迷途',85],['小布丁',65],['附录娃娃','95'],['怡静',90]]
result=False 
for each in score:
    if name==each[0]:
        print(name+"的得分是:",each[1])
        result=True
        break
if not result:
    print("查找的数据不存在")

