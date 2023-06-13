'''
Author: Amos Cao
Date: 2023-03-15 11:24:44
LastEditors: Amos Cao
LastEditTime: 2023-03-15 11:42:28
Description: sad代码dog
'''
#使用该模块中的ClientSession对象
import requests
import asyncio
import time
import aiohttp

start = time.time()
urls = ["https://www.baidu.com","https://www.baidu.com","https://www.baidu.com","https://www.baidu.com"]

async def get_page(url):
    print("download start")
    # requests是基于同步，必须使用基于异步的网络请求模块进行执行url的请求发送
    #aiohttp：基于异步网络请求的模块
    # response = requests.get(url=url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            # text() 返回字符串形式的响应数据
            # read() 返回二进制形式的响应书记
            # json() 返回的就是json对象
            text = await response.text()
    await asyncio.sleep(2)
    print("download success")

tasks = []
for url in urls:
    c=get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end-start)