class Turtle:   #  类对象，类名约定是以大写的字母开头的。对象是可以基于类对象进行量产的
    color="green"
    weight=10
    legs=4
    shell=True
    mouth="大嘴"
    # 定义方法
    def climb(self):
        print("我正在很努力的往前爬")

    def run(self):
        print("我正在飞快的往前爬")
    
    def  bite(self):
        print("咬死你咬死你")
    def eat(self):
        print("有的吃，真满足")
    def sleep(self):
        print("困了，睡了，晚安")
