# 使用requeusts获取整个网页的HTML信息；
# 使用Beautiful Soup解析HTML信息，找到所有<img>标签，提取src属性，获取图片存放地址；
# 根据图片存放地址，下载图片。




# -*- coding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    target = 'https://unsplash.com/'
    req = requests.get(url=target)
    # req.encoding = ('utf-8')
    # input(req.text)

    html = req.text  #先把内容赋值给 'html'变量
    bf = BeautifulSoup(html)    #然后用BeautifulSoup解析
    img = bf.find_all('img',class_ = "IEpfq")
    input(img)