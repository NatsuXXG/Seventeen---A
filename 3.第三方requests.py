
# 引入第三方插件 
import requests

r = requests.get('https://api.github.com/events')
r.encoding = ('utf-8')
# print(r.text)
# print(r.encoding)
# print(r.content)
# print(r.status_code)
# print(r.headers)
# print(r.json())
print(r.raw.read(10))













