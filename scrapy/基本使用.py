#高性能的持久化存储，异步的数据下载，高性能的数据解析，分布式

#scrapy startproject firstBlood 新建工程
# cd 到工程中
#scrapy genspider first www.xxx.com 新建文件
# scrapy crawl first --nolog 执行工程 --nolog可以让log不显示

# scrapy crawl first -o ./test/baidu.csv终端持久化操作

# 基于管道持久化
# 数据解析-在item类中定义相关的属性-将解析的数据封装存储到item类型的对象 - 将item类型的对象提交给管道进行持久化存储的操作 - process_item中处理 - 在配置文件中开启管道

# 基于Spiderl的全站数据爬取
# 就是将网站中某板块下的全部页码对应的页面数据进行爬取
# 实现方式：
# 将所有页面的urL添加到start_urLs列表（不推荐）
# 自行手动进行请求发送（推荐）
# 手动请求发送：
# yield scrapy.Request(urL,callback):callback专门用做于数据解析


# ImagesPipeline:
# -只需要将img的src的属性值进行解析，提交到管道，管道就会对图片的src进行请求，获取图片二进制数据

# 中间件
#   一下载中间件
#     位置：引擎和下载器之间
#     作用：批量拦截到整个工程中所有的请求和响应
#   一拦截清求：
#     UA伪装
#     代理IP
#  拦截响应：
#  篡改响应数据，响应对象

# CrawlSpider:类，Spider的一个子类
#     全站数据爬取的方式
#         -基于Spider:手动请求
#         -基于CrawlSpider
#     CrawlSpider的使用：
#         创建一个工程
#         cd XXX
#         创建爬虫文件(CrawlSpider):
#             scrapy genspider -t crawl xxx www.xxxx.com
#             链接提取器：
#                 -作用：根据指定的规则(allow)进行指定链接的提取
#             规则解析器：
#                 -作用：将链接提取器提取到的链接进行指定规则(callback)的解析
#         #需求：爬取su网站中的编号，新闻标题，新闻内容，标号
#             分析：爬取的数据没有在同一张页面中。
#             1,可以使用链接提取器提取所有的页码链接
#             2,让链接提取器提取所有的新闻详情页的链接