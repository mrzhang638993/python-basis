from tkinter import *


def callback():
    var.set("吹吧你,我才不信了")


root = Tk()
# 实例化tkinter的变量
var = StringVar(master=root)
var.set("您下载的内容含有未成年人限制信息\n，请满18周岁后点击观看")
photo = PhotoImage(file="bg.gif")
frame = Frame(master=root)
frame.pack(padx=10, pady=10,side=BOTTOM)
frame2 = Frame(master=root)
frame2.pack(padx=10, pady=10,side=BOTTOM)
theLable = Label(master=root,
                 image=photo,
                 justify=LEFT,
                 textvariable=var,
                 compound=CENTER,
                 font=('华康少女字体', 20),
                 fg="white")
theLable.pack()
# button的绝大多数的信息和label是一样的
button = Button(frame,text="我已满18周岁", command=callback,width=20)
button.pack(side=BOTTOM)
root.mainloop()
