import easygui as g
title="账号中心"
msg='【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail】为必填项'
# 下面开始输入框的处理
fileNames=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
g.multenterbox(msg,title,fileNames)

"""
提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
"""
import  easygui as g
filePath=g.fileopenbox()
with open(filePath,'rt',encoding='UTF-8') as f:
    print(f.read())

"""
在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能
"""
import  easygui as g
filePath=g.fileopenbox()
with open(filePath,'rt',encoding='UTF-8') as f:
    print(f.read())
