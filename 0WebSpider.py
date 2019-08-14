
import requests   #还是一样 先引入第三方请求插件
from bs4 import BeautifulSoup  #引入第三方解析

if __name__ == "__main__":
    server = 'https://www.biqukan.com/'
    target = 'https://www.biqukan.com/1_1094/' #请求的网址
    req = requests.get(url = target)    #requests的get方法 
    req.encoding=('gbk')
    html = req.text     #请求到的text 赋值给html

    div_bf = BeautifulSoup(html)    #解析
    div = div_bf.find_all('div',class_='listmain') #根据解析到的去匹配
    # print(div[0])

    # 接下来再匹配多一次!
    a_bf = BeautifulSoup(str(div[0])) 
    a = a_bf.find_all('a') 

    for each in a :
        #用循环的方式 先输出一条'讯息'里面的'字符串'(string)
        #,逗号隔开后,  用之前的网页路径名 + 相对路径名字 用get得到a 的href
        print (each.string ,  server + each.get('href'))

#👆 以上的筛选方式 都是要根据 网站的结构来筛选的
#👆 以上是抓取静态网页的基础
#基础




#接下来的笔记的 关于  动态网页的  抓包 👇

#👇用抓包工具
#对于初学者，我们不必看懂JavaScript执行的内容是什么，做了哪些事情，因为我们有强大的抓包工具，它自然会帮我们分析。这个强大的抓包工具就是Fiddler：http://www.telerik.com/fiddler