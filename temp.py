number=input("请输入一个整数(输入Q结束程序):")
if number.isdigit():  #  input输入的话，对应的使用是字符串的，需要进行处理
    dest=int(number)
    print("十进制->十六进制  : ","%#x" % dest)
    print("十进制->八进制  : ","%#o" % dest)
    print("十进制->二进制  : ",bin(dest))
else:
    print("输入错误，请重新输入")
    number=input("请输入一个整数(输入Q结束程序):")

