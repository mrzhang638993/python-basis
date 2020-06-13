# 使用有道词典进行翻译
import gzip
import json
from io import BytesIO
from urllib import parse
from urllib import request
import  time

"""
#  有道翻译已经改版了，需要进行加密操作处理的。需要破解相关的加密和解密的操作机制的
# 需要破解相关的加密机制的，还有就是访问的测试过多的话，对应的对方会将你的访问信息拉黑的。
# python 对应的存在拉黑的机制的，对应的需要进行管理操作的。
# 程序可以正常的执行和投入到生产的环境信息的，检查的操作对应的是agent的操作的，对应的需要进行隐藏的。需要模拟正常的浏览器访问的。
#  每一次请求的salt这些信息都不是一样的，怎么进行处理？对应的请求的salt对应的都是不断的变化的
# 单位时间内访问的次数超过了限制次数的话，认为其对应的是一个爬虫的操作的，需要进行关闭操作的。
解决办法：延迟提交的时间，让爬虫看起来像一个正常的请求操作。或者是使用代理的方式实现操作的。
"""
"""
修改header的方法包括如下的方式和路径：
1.在生成Request对象生成的时候进行处理即可；
2.Request对象生成之后，对应的执行add_header()方法对应的增加即可实现。
"""
while True:
    con = input("请输入需要翻译的内容:输入q!退出程序")
    if con == 'q!':
        break
    else:
        url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        data = {}
        headers = {}
        headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        headers['Accept-Encoding'] = 'gzip, deflate'
        headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
        headers['Connection'] = 'keep-alive'
        headers['Content-Length'] = '237'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers[ \
            'Cookie'] = 'OUTFOX_SEARCH_USER_ID=1734023566@10.108.160.17; JSESSIONID=aaaQf0xlyKo3FdOA9BRkx; OUTFOX_SEARCH_USER_ID_NCOO=219410896.8655732; ___rl__test__cookies=1592017877920'
        headers['Host'] = 'fanyi.youdao.com'
        headers['Origin'] = 'http://fanyi.youdao.com'
        headers['Referer'] = 'http://fanyi.youdao.com/'
        headers[ \
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        data['i'] = con
        data['from'] = "AUTO"
        data['to'] = "AUTO"
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '15920178779302'
        data['sign'] = '14bec33cc4681dd9bf4212c25c475214'
        data['ts'] = '1592017877930'
        data['bv'] = 'c74c03c52496795b65595fdc27140f0f'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTlME'
        # uniode 转化为utf-8的形式
        try:
            data = parse.urlencode(data).encode("utf-8")
            req = request.Request(url=url, data=data, headers=headers)
            response = request.urlopen(req, timeout=200)
            content = response.read()
            buff = BytesIO(content)
            f = gzip.GzipFile(fileobj=buff)
            html = f.read().decode('utf-8')
            content = json.loads(html)
            print("翻译的结果是:%s" % (content['translateResult'][0][0]['tgt']))
            # 等待5秒中之后才可以执行后续的操作的
            time.sleep(5)
        except Exception as reason:
            print(reason)
