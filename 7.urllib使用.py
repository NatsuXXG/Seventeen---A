

# request：它是最基本的 HTTP 请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入 URL 以及额外的参数，就可以模拟实现这个过程了。
# error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。
# parse：一个工具模块，提供了许多 URL 处理方法，比如拆分、解析、合并等。
# robotparser：主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。



## 引入 urllib库的request
import urllib.request 

## 请求随便一个网址    urlopen??? 链接打开???
response = urllib.request.urlopen('https://www.python.org')  
##用过以上式子    返回的是一个👇
print(type(response))
## 一个 HTTPResposne 类型的对象，主要包含 read、readinto、getheader、getheaders、fileno 等方法，以及 msg、version、status、reason、debuglevel、closed 等属性。
## 得到这个对象之后，我们把它赋值为 response 变量，然后就可以调用这些方法和属性，得到返回结果的一系列信息了。
## 例如，调用 read 方法可以得到返回的网页内容


## 打印一下 read?? 是什么意思   decode意思应该是为utf-8的格式 打印出来 read    上面请求后出来可读的东西
# print(response.read().decode('utf-8'))


print(response.status)                #响应码
print(response.getheaders())          #得到头文件信息
print(response.getheader('Server'))   #传入Server 参数 看看 服务器的上面搭建的     (服务器是由nginx搭建的)

