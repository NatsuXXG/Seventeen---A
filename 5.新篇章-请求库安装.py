# https://python3webspider.cuiqingcai.com/1.2-qing-qiu-ku-de-an-zhuang 
# 根据以上网站学习



# 1、 requests 的安装     
# pip3 install requests



# 2、 Selenium 是一个自动化测试工具，
# 利用它我们可以驱动浏览器执行特定的动作，如点击、下拉等操作。
# 对于一些 JavaScript 渲染的页面来说，这种抓取方式非常有效。
# 下面我们来看看 Selenium 的安装过程。


# from selenium import webdriver
# browser = webdriver.Chrome()

from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)



#3、 aiohttp 的安装
# 之前介绍的 requests 库是一个阻塞式 HTTP 请求库，当我们发出一个请求后，程序会一直等待服务器响应，直到得到响应后，程序才会进行下一步处理。其实，这个过程比较耗费时间。如果程序可以在这个等待过程中做一些其他的事情，如进行请求的调度、响应的处理等，那么爬取效率一定会大大提高。
# aiohttp 就是这样一个提供异步 Web 服务的库，从 Python 3.5 版本开始，Python 中加入了 async/await 关键字，使得回调的写法更加直观和人性化。aiohttp 的异步操作借助于 async/await 关键字的写法变得更加简洁，架构更加清晰。使用异步请求库进行数据抓取时，会大大提高效率，下面我们来看一下这个库的安装方法。