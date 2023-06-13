import scrapy
from imagePro.items import ImageproItem


class ZhanzhangSpider(scrapy.Spider):
    name = "zhanzhang"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]

    def parse(self, response):
        # print(response.text)
        div_list = response.xpath('/html/body/div[3]/div[2]/div')
        for div in div_list:
            src = 'https:'+div.xpath('./img/@data-original').extract_first()
            item = ImageproItem()
            item['src'] = src
            print(src)
            yield item
