##list1=[1,3,5,7,9]
##list2=[2,4,6,8,10]
##def assemble1(x,y):
##    return [x,y]
##listResult=list(map(lambda  x,y:assemble1(x,y),list1,list2));
##print(listResult)
##def make_repeat(n):
##        return lambda s : s * n
##
##double = make_repeat(2)  # s->s*2   double=16
##print(double(8))
##print(double('FishC'))
##def power1(x,y):
##    if y==1:
##        return x
##    else:
##        return x*power1(x,y-1)
##print(power1(2,3))
#  递归函数
#gcd(x, y)

# 求解的是x,y中的最大的公约数
##def gcd1(x,y):
##    if x<y:  # x是最大的，y是最小的
##        x,y=y,x
##    # 求解最大的公约数
##    if x%y==0 :
##        return y
##    else:
##       gcd1(y,x%y)    
##print(gcd1(12,18))
##def find_divisor(a,b):
##    '''这个函数用来求两个正整数的最大公约数'''
## 
##    #下面的操作保证a永远是较大的数，这样对于我们传参的要求就低了，传入数字的大小顺序无所谓
##    if a<b:
##        a,b=b,a
##    #下面是基线条件，当余数为0时，b就是最大公约数
##    if a%b==0:
##        return b
##    #不符合基线条件时，就要继续寻找最大公约数，但是参数要变成b和ab的余数，实现递归
##    else:
##        return find_divisor(b,a%b)
##print(find_divisor(88,24))
##
##def   diguiqiujie(n):
##    if n//2==0:
##        return n%2
##    else:
##        return str(n%2)+str(diguiqiujie(n//2))
##print(diguiqiujie(5))
##def diguifenjie(n):
##    global list1
##    if n//10==0:
##        list1.insert(0,n%10)
##    else:
##        list1.insert(0,n%10)
##        n //=10
##        diguifenjie(n)
##list1=[];
##diguifenjie(12345)
##print(list1)
##def huiwenzifuchuan(ch):
##    length=len(ch)
##    if  not ch[0]==ch[length-1]:
##        return "不是回文字符串"
##    elif length==2 and ch[0]==ch[1]:
##        return "是回文字符串"
##    else:
##        return huiwenzifuchuan(ch[1:length-1])
##print(huiwenzifuchuan("我是谁"))
def  caculateYear(n):
    if n==1:
        return 10
    else:
        return 2+caculateYear(n-1)
print(caculateYear(5))

