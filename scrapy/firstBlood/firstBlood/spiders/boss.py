'''
Author: Amos Cao
Date: 2023-03-21 10:26:40
LastEditors: Amos Cao
LastEditTime: 2023-03-22 09:38:37
Description: sad代码dog
'''
# import scrapy
# from firstBlood.items import BossItem
# from time import sleep

# class BossSpider(scrapy.Spider):
#     name = "boss"
#     # allowed_domains = ["www.xxx.com"]
#     start_urls = ["https://www.ncss.cn/student/jobs/index.html?jobName=python"]

#     def parse_detail(self, response):
#         # item = response.meta['item']
#         print("aaa")
#         # # print(response.text)
#         # job_desc = response.xpath('//*[@id="root"]')
#         # print(job_desc)
#         # item['job_desc'] = job_desc

#     def parse(self, response):
#         print(response.text)
#         li_list = response.xpath('//*[@id="jobLIST"]/div')
#         print(li_list)
#         for li in li_list:
#             job_name = li.xpath('./div[1]/ul/h5/a/@title').extract_first()
#             url = li.xpath('./div[1]/ul/h5/a/@href').extract_first()
#             print(job_name,url)
#             item = BossItem()
#             item['job_name'] = job_name
#             # 请求传参 meta字典
#             yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item': item})
