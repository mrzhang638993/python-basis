from tkinter import *

root = Tk()
lable = Label(master=root,
              text="您下载的内容含有未成年人限制信息，请满18周岁后点击观看",
              justify=RIGHT,
              padx=10,
              pady=10)
# 对文本进行描述,之后才可以看到相关的内容的
lable.pack()
# 要求源文件必须是gif，png等的格式操作的
photo = PhotoImage(file="18.gif")
images = Label(master=root, image=photo)
images.pack(side=RIGHT)
root.mainloop()

