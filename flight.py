# 打飞机游戏的加载流程
步骤一: 加载背景音乐
步骤二: 播放背景音乐
步骤三:
    创建飞机
    我方飞机是全局性的飞机的。敌方飞机是循环的飞机的,不断的循环产生的。
    定义小飞机的间隔，只有满足指定的要求对应的才会创建飞机的。
interval=0
while True:
    if 用户点击了关闭按钮:
        退出程序
    interval+=1
    if interval==50:
        interval=0
        小飞机诞生
    #屏幕对应的不断的刷新操作
    小飞机移动一个位置
    屏幕刷新
    if 用户鼠标位置产生移动:
        我方飞机中心位置=用户鼠标位置
        屏幕刷新
    if  我方飞机与小飞机发生肢体冲突:
        我方挂了，播放撞击音乐
        修改我方飞机图案
        打印"Game over"
        停止背景音乐，最好淡出
    
    