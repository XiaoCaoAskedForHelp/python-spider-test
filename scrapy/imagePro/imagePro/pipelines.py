# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImageproPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     print(item)

    # 可以根据图片地址进行请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'],dont_filter=True)
    
    #指定图片存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        return imgName
    
    
    def item_completed(self, results, item, info):
        return item #返回给下一个即将被执行的管道类