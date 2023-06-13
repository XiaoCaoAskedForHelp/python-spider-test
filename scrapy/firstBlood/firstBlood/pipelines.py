'''
Author: Amos Cao
Date: 2023-03-20 09:52:43
LastEditors: Amos Cao
LastEditTime: 2023-03-20 14:00:40
Description: sad代码
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstbloodPipeline:
    fp = None
    def open_spider(self,spider):
        print('开始爬虫....')
        self.fp = open('./test/baidu.txt','w',encoding='utf-8')


    # 处理item类型的对象，没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        title = item['title']
        url = item['url']

        self.fp.write(title+":"+url+'\n')
        return item  # 传递给下一个即将被执行的管道类
    

    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()



class mysqlbloodPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp = open('./test/mysql.txt','w',encoding='utf-8')


    # 处理item类型的对象，没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        title = item['title']
        url = item['url']

        self.fp.write("mysql:"+title+":"+url+'\n')
        return item
    

    def close_spider(self,spider):
        self.fp.close()

#怕从文件提交的item类型会提交给优先级较高的管道类

class printPipeline:
    # 处理item类型的对象，没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        print(item)
        return item