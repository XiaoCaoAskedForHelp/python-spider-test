import requests;
from lxml import etree;
import random
from multiprocessing.dummy import Pool
# https://www.pearvideo.com/category_1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
url = 'https://www.pearvideo.com/category_1'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    # 注意：视频链接不完整，需要拼接
    detail_url = "https://www.pearvideo.com/" + li.xpath("./div/a/@href")[0]
    # 获取的标题文本，后面加上视频格式后缀".mp4"
    name = li.xpath("./div/a/div[2]/text()")[0]+".mp4"
    # print("url:",detail_url)
    # print("name:"+name)
    # 对详情页的url发请求并获取响应数据
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    # 从前面详情页数据中解析出的"video_1746440"中分离出1746440这一部分，作为params中的contId
    cont_Id = li.xpath("./div/a/@href")[0].split("_")[-1]
    # 封装好get请求的参数，"mrd"是一个介于0和1之间的随机数，用random模块下的random()方法，注意要转成字符串类型
    print("cont_Id:",cont_Id)
    params = {"contId": cont_Id, "mrd": str(random.random())}
    # 加了'Referer': 'https://www.pearvideo.com/video_1746440'后就不会显示该文章已下架了
    ajax_headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
        "Referer":
            "https://pearvideos.com/video_" + cont_Id
        }
    # 对ajax中的视频链接发起请求，并获取响应数据，注意响应数据的类型是json类型，返回的是一个字典！！
    ajax_url = "https://www.pearvideo.com/videoStatus.jsp"
    ajax_data = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
    # print(ajax_data)
    video_url = ajax_data["videoInfo"]['videos']["srcUrl"]
    # print("video_url" + video_url)

    # 但解析出来的视频地址是一个加密后的伪地址，需要将中间的一串13位数字改成cont-cont_id，方可得到真地址
    # 伪地址：https://video.pearvideo.com/mp4/third/20211123/1638172217395-12719568-193109-hd.mp4
    # 真地址：https://video.pearvideo.com/mp4/third/20211123/cont-1746440-12719568-193109-hd.mp4

    # 先将伪地址用"/"切割为列表,['https:', '', 'video.pearvideo.com', 'mp4', 'third', '20211123', '1638180827144-12719568-193109-hd.mp4']
    list1 = video_url.split("/")
    # 取出列表中的最后一个字符串：'1638180827144-12719568-193109-hd.mp4',将其用"-"切割为列表
    # ['1638180827144', '12719568', '193109', 'hd.mp4']
    list2 = list1[-1].split("-")
    # 用"cont-1746440"替换掉列表中的第一个字符串：'1638180827144'
    list2[0] = "cont-" + cont_Id
    # 用-把list2中的元素连接成一个字符串再替换list1中的最后一个元素
    list1[-1] = "-".join(list2)
    # 再将list1中的元素连成一个字符串就搞定了
    video_url_valid = "/".join(list1)
    print(video_url_valid)  #测试无误！！！
    dict = {
        'name': name,
        "url": video_url_valid
    }
    urls.append(dict)

def get_video_data(dic):
    url = dic["url"]
    print(dic["name"],"download start")
    data = requests.get(url=url,headers=headers).content
    with open('./test/异步爬虫/梨视频/' + dic["name"],"wb") as fp:
        fp.write(data)
        print(dic["name"],"download success")

pool = Pool(4)
pool.map(get_video_data,urls)

# 关闭子线程
pool.close()
# 关闭主线程
pool.join()
