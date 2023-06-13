'''
Author: Amos Cao
Date: 2023-03-23 10:36:37
LastEditors: Amos Cao
LastEditTime: 2023-03-23 10:52:28
Description: sad代码dog
'''
import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["www.xx.com"]
    start_urls = ["https://news.163.com/"]

    modules_urls = []
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[3]/div[2]/div[5]/div/div[1]/ul/li')
        # print(li_list)
        alist = [2,3]
        for index in alist:
            module_url = li_list[index].xpath('./a/@href').extract_first()
            print(module_url)
            self.modules_urls.append(module_url)

        #依次对每一个板块对应的页面进行请求
        for url in self.modules_urls:
            yield scrapy.Request(url,callback=self.parse_module)


    def parse_module(self, response):
        pass
