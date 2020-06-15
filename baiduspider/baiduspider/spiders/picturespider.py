# 爬虫的相关的操作和实践操作,需要待定操作实现
import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baiduspider"
    allow_domains = ['baidu.com']
    start_urls = ['https://image.baidu.com/']

    def parse(self, response):
        filename = response.url.split("/")
        with open('result.txt', 'wb')  as f:
            f.write(filename)
