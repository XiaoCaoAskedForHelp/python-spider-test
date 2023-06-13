'''
Author: Amos Cao
Date: 2023-03-20 09:55:51
LastEditors: Amos Cao
LastEditTime: 2023-03-20 13:29:01
Description: sad代码dog
'''
'''
Author: Amos Cao
Date: 2023-03-20 09:55:51
LastEditors: Amos Cao
LastEditTime: 2023-03-20 10:07:58
Description: sad代码dog
'''
import scrapy
from firstBlood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称： 就是爬虫源文件的一个唯一标识
    name = "first"
    #允许的域名: 用来限定start urls列表中哪些url可以进行请求发送
    # allowed_domains = ["www.xxx.com"]
    # 起始的url列表，该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ["https://www.baidu.com/"]

    
    #用作与数据解析：response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        # print(response)
        # print(response.text)
        all_data = [] 
        li_list = response.xpath('//*[@id="hotsearch-content-wrapper"]/li')
        for li in li_list:
            # xpath 返回的是列表，但是列表元素一定是selector类型的对象
            # extract可以将每一个Selector对象中data参数存储的字符串提取出来，形成一个数组
            title1 = li.xpath('./a/span[2]/text()').extract()
            url = li.xpath('./a/@href').extract_first()

            title = ','.join(title1)
            
            print(title,url)

            # dic = {
            #     'title': title,
            #     'url': url
            # }
            # all_data.append(dic)

            item = FirstbloodItem()
            item['title'] = title
            item['url'] = url

            yield item # 将item提交给管道

        # return all_data
