# 爬虫，获取妹子的图片的操作
import  urllib.request
import  os


def get_page(url):
    pass

# 获取所有的下载链接
def get_all_page_ref(url):
    pass
def download_mm(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url="http://jandan.net/ooxx"
    page_num=int(get_page(url))
    # 需要重新请求获取到更多的链接地址信息的
    # 需要获取所有的网站的链接操作
    urls=get_all_page_ref(url);





