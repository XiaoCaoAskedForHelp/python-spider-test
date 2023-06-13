import requests;
from lxml import etree;

url = 'https://cn.bing.com/search?q=本机ip'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
}

# python3.8以下版本：
# proxies{' 要请求网站的协议类型 ' , ' 代理服务器ip : 端口 '}
# python3.8以上版本：
# proxies{' 要请求网站的协议类型 ' , ' "代理服务器类型(http/https/socks5)://代理服务器ip : 端口 '}

page_text = requests.get(url=url,headers=headers,proxies={"https": "61.154.91.111:29028"},timeout=30).text
with open('./test/验证码/代理.html','w',encoding="utf-8") as fp:
    fp.write(page_text)

tree = etree.HTML(page_text)

ip = tree.xpath('//*[@id="b_results"]/li[1]/div[2]/text()')[0]
print(ip)

# 代理ip的透明度
# 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
# 匿名：知道使用了代理，不知道真实ip
# 高匿：不知道使用了代理，也不知道真是ip

# SSL异常：

#      requests.exceptions.SSLError: HTTPSConnectionPool(host='119.139.198.65', port=3128): Max retries exceeded with url: http://icanhazip.com/ (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'ssl3_get_record', 'wrong version number')])")))
# 　　　　问题来源：使用的IP地址 是Http类型的  没有进行SSL加密

# 　　　　解决：更换IP   来源 ：https://www.xicidaili.com/  ；https://www.kuaidaili.com/free/

# 　　2.　　requests.exceptions.ChunkedEncodingError: ("Connection broken: ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None)", 　　　　　　ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))

# 　　　问题来源：该地址 在抓取验证过程中人被判定为有效，但是在使用的时候已经超过生命周期

# 　　　解决：换地址

# 　　3　　requests.exceptions.ProxyError: HTTPSConnectionPool(host='47.104.172.108', port=8118): Max retries exceeded with url: http://icanhazip.com/ (Caused by 　　　　　　　　ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 503 Too many open connections')))
# 　　　　　
# 　　　　（部分）问题来源：ip和HTTP类型但是强行使用https协议