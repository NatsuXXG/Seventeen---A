# -*- conding=utf-8  -*- 
# 本页 是用于 练习 爬取 https://www.biqukan.com/1_1094/ 此小说的目录练习


import requests , sys   #还是一样 先引入第三方请求插件
from bs4 import BeautifulSoup  #引入第三方解析

"""
类说明:下载《笔趣看》网小说《一念永恒》
"""

class downloader(object):

    def __init__(self):    #初始化
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'   #1_1094是《一念永恒》是网址
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数



    def get_download_url(self):
        req = requests.get(url = self.target)   #请求链接
        req.encoding=('gbk')
        html = req.text                         #文本
        div_bf = BeautifulSoup(html)            #解析
        div = div_bf.find_all('div', class_ = 'listmain')   #解析后筛选
        a_bf = BeautifulSoup(str(div[0]))                   #然后再解析
        a = a_bf.find_all('a')                              #再解析后去筛选a标签
        self.nums = len(a[15:17])                                #剔除不必要的章节，并统计章节数  #a标签15以后 页码的总页数 = a 15 以后的长度   #(实验为了节约时间 所以只选择两章)
        for each in a[15:17]:   
            self.names.append(each.string)                   #网页的章节名字.添加 (遍历一条出来的)
            self.urls.append(self.server + each.get('href')) #网页的url链接




    def get_contents(self, target):         
        req = requests.get(url = target)    #根据参数里的链接 发出请求
        req.encoding=('gbk')
        html = req.text                     #得到内容
        bf = BeautifulSoup(html)            #解析.....  
        texts = bf.find_all('div', class_ = 'showtxt') #筛选内容
        texts = texts[0].text.replace('\xa0'*8,'\n') #用text属性 滤除<br> 这些标签  然后还要用'\n\n'(回车) replace(替代) - '\xa0'占位符八个
        return texts                            #最后返回texts


    def writer(self, name, path, text):   
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
