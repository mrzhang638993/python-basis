# 爬虫的相关的机制和实现逻辑
from urllib import request

response = request.urlopen("http://www.fishc.com")
# 获取二进制的数据
html = response.read()
# 进行资源的解密操作和实现
html = html.decode("utf-8")
print(html)
