# re是ptyhon 的一个用来正则的模块
import re

content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*(\d+)\s.*s$',content)
print(res.group(1))