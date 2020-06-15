import tkinter as tk


class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        # 调整框架的位置
        frame.pack(side=tk.LEFT, padx=20, pady=30)
        self.hi_there = tk.Button(frame,
                                  text="打招呼",
                                  fg="blue",
                                  command=self.sayhi,
                                  background="yellow",
                                  foreground="black")
        self.hi_there.pack()

    def sayhi(self):
        print("互联网的广大朋友们，我是小甲鱼")


root = tk.Tk()
app = App(root)
root.mainloop()
