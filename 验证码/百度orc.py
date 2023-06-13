'''
Author: Amos Cao
Date: 2023-03-13 13:45:35
LastEditors: Amos Cao
LastEditTime: 2023-03-14 10:44:14
Description: sad代码dog
'''
import requests
from lxml import etree
import base64
import urllib

API_KEY = "0nw9iqHpTv5PgQEAzpOG81LO"
SECRET_KEY = "DpGbdQSoNtjbwEgkSFCPcePfUw8olylx"

# 保存cookie
# session = requests.Session()
# session.post()

def main():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)

    code_img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    print(code_img_src)
    img_data = requests.get(url=code_img_src,headers=headers).content
    with open('./test/验证码/code.jpg','wb') as fp:
        fp.write(img_data)

    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + get_access_token()
    
    payload='image=' + get_file_content_as_base64("./test/验证码/code.jpg",True)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()