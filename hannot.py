def hanoi(n,x,y,z):
    if n==1:
        print(x,'----->',z)
    else:
        hanoi(n-1,x,z,y) # 移动从x到y的
        #  需要将前面的n-1个盘子从x移动到y上面
        #print(x,'------->',y)
        #下面需要将第n个盘子从x移动到z上面的
        print(x,'---------->',z)
        # 最后需要将后面的n-1个盘子从y移动到z上面的
        hanoi(n-1,y,x,z)
n=int(input('请输入汉罗塔的层数:'))
hanoi(n,'x','y','z')

        
