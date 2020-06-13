# -*- coding:utf-8 -*-
from urllib import request

response = request.urlopen("http://placekitten.com/200/300")
print(response.geturl())
print(response.info())
# 获取http的状态码信息
print(response.getcode())
content = response.read()
with open("cat.img", 'wb') as f:
    f.write(content)
