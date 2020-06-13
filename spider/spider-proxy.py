from urllib import request

import brotli
import  random

"""
1.使用代理方式访问，需要增加头信息的
"""
url = "https://www.whatismyip.com/"
headers = {}
iplist=['192.168.1.101:80']
headers['authority'] = 'www.whatismyip.com'
headers['method'] = 'GET'
headers['path'] = '/'
headers['scheme'] = 'https'
headers[
    'accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['accept-encoding'] = 'gzip, deflate, br'
headers['accept-language'] = 'zh-CN,zh;q=0.9'
headers['cache-control'] = 'max-age=0'
headers[
    'cookie'] = '__cfduid=dfb3a167048046dedf70a3f5f6907c01f1592033774; dwqa_anonymous=kl7qcEv2ExYi4160oQsSJBzu8ZeA4g2QQBfs5kkKpFl; session_id=d33d0f5f-dd34-4bf3-9933-4be691e20642; _ga=GA1.2.1891763902.1592033779; _gid=GA1.2.404374399.1592033779; cto_bidid=EgIpXl81MVIxcGFMcWF0JTJGUlQlMkIlMkZWSWJYRnRnMzBVMWFCRXpSZUVyeHlNcVlYMDgwU3d1WWVKdXVEc0RJZHpHSkdXSFA3U2dHU3RHa3ZTNHpvWEM2VnRCR1FDczBwanROVTZsZ1ZYZnpJcjNTRkFGMCUzRA; cto_bundle=Rya_pV83c2NhZ0NRVFlJV0FoaHNmYlAwQTFBQTZ1enRGUlpTWXpRS0VGczkzVDJFbkZFckE2dlRqRVkxdFZ0TXNwVlZ5bloweTc3dkVGTkkweW9oR2ZxV3lqNDNPWldMSW1RMXRJWEloVWkyM0R4JTJCTXRhZEh3ZTRZQWtMRmpsYW94SVpab3M0dURja2hnTnhhNWVSWmtFa1dhZyUzRCUzRA; __gads=ID=f82c837e7d139f23:T=1592033780:S=ALNI_MaH_Fmtj0mKduzrUGKbgFqPwgTO2A; _gat=1'
headers['sec-fetch-dest'] = 'document'
headers['sec-fetch-mode'] = 'navigate'
headers['sec-fetch-site'] = 'none'
headers['sec-fetch-user'] = '?1'
headers['upgrade-insecure-requests'] = '1'
headers[
    'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
#  步骤一：创建代理服务器
req = request.Request(url=url, headers=headers, method='GET')
proxy_support = request.ProxyHandler({'http': random.choice(iplist)})
# 步骤二： 创建opener
opener = request.build_opener(proxy_support)
# opener.addheaders()
# 步骤三：安装opener
request.install_opener(opener)
# 开始代码的访问操作
response = opener.open(req)
encoding = response.getheader('Content-Encoding')
if encoding == 'br':
    html = response.read()
    content = brotli.decompress(html).decode('UTF-8')
    # 对应的怎么从html文档中获取到相关的内容过滤操作需要对应的正则和相关的匹配操作的
    print(content)
