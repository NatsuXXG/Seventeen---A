#coding=utf-8

# 用第三方的请求库 requests 下载安装方式是 pip install requests
import requests
# BeautifulSoup 翻译过来是'美丽的汤' 他的作用是解析出我们爬取到的html内容
from bs4 import BeautifulSoup

# 下面是一个请求的基础过程 记住就好 先不理解 (所谓:抓取)
if __name__ == '__main__':
    target = 'https://www.biqukan.com/1_1094/5403177.html' #这是请求的url网址
    req = requests.get(url=target)  #这是用到第三方库requests的get方法
    req.encoding=('gbk')    #这是为了防止乱码 使用请求的这个网站的chatset的格式

    # print(req.text)     #这一下是把爬取到的html内容print输出出来



#👇接下来 我们要把爬取到的html 解析 提取出我们要的内容👇 (所谓:筛选)
html = req.text  #先把内容赋值给 'html'变量
bf = BeautifulSoup(html)    #然后用BeautifulSoup解析
texts = bf.find_all('div', class_ = 'showtxt')  #然后用bf内置的find_all方法 筛选出来

# print(texts)    #然后输出打印一下
print(texts[0].text.replace('\xa0'*8,'\n\n'))    #使用text属性,提取文本内容,滤除<br>标签,然后用replace,去除空格-替换成回车