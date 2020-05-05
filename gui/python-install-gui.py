# 安装gui的相关的操作
"""
1.下载源码包:
2.执行  python   setup.py  install 
"""
#from  easygui  import *   #  导入虽有的easygui的lib
#  建议方式如下:
import easygui   as g
import  sys


while 1:
    g.msgbox("嗨，欢迎进入第一个界面小程序")
    msg="请问你希望在鱼C工作室学习到什么知识呢？"
    title="小游戏互动"
    choices=['谈恋爱','编程','OOXX','琴棋书画']
    choice=g.choicebox(msg,title,choices)

    g.msgbox("你的选择是:"+str(choice),'结果')
    msg="你希望重新开始小游戏吗？"
    title="请选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
