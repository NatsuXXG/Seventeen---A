
from urllib import request,parse
import ssl

context = ssl._create_unverified_context()

#接着定义一下我们的请求 url 和 header
url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    #假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}


#再定义一下我们的请求参数
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'NatsuXXG',
    'password':'XXG12138',
    '_post_type':'ajax',
}

#我们把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')

#然后我们就可以封装 request 了
req = request.Request(url,data=data,headers=headers,method='POST')

#最后我们进行请求
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))








