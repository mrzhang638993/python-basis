#  not>and>or
i=1
while True:
    if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
        print("步数是如下的:",i)
        break
    else:
        i +=1
