import scrapy


class MiddleSpider(scrapy.Spider):
    name = "middle"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["http://www.baidu.com/s?wd=ip"]

    def parse(self, response):
        print(response.text)
