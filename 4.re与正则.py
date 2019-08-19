# re是ptyhon 的一个用来正则的模块
import re

content = 'Xiaoshuaib has 100 bananas'   

res = re.match('^Xi.*(\d+)\s.*s$',content)              # match(配对)
res = re.match('^Xi.*?(\d+)\s.*s$',content)             #  '?'贪婪匹配 (贪婪匹配就是一个一个去匹配)
res = re.match('^Xi.*?(\d+)\s.*s$',content,re.S)        # re.S匹配有换行的

res = re.search('^Xi.*?(\d+)\s.*s$',content,re.S)       # re.search 匹配成功的第一个结果返回
res = re.findall('^Xi.*?(\d+)\s.*s$',content,re.S)      # re.findall 匹配所有相关的

content = re.sub('\d+','250',content)                   #  re.sub  第二个参数替换掉 第一个匹配到的东西


pattern = re.compile('Xi.*?(\d+)\s.*s',re.S)            # re.comile  用来封装一下 便于以后调用
res = re.match(pattern,content)


print(res.group(1))
















