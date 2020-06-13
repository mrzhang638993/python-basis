# 使用有道词典进行翻译
import gzip
import json
from io import BytesIO
from urllib import parse
from urllib import request
import  time

"""
使用代理服务器进行数据的代理操作和实现
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
