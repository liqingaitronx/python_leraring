import urllib.request as ur
url = 'https://taobao.com/'#请求的URL
headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
           'AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/108.0.0.0 Safari/537.36',
           'Referer': 'https://www.baidu.com/',
           'Connection': ' keep-alive'
           }#定义请求头
#设置request请求头
re = ur.Request(url,headers=headers)
#使用urlopen请求
html = ur.urlopen(re).read().decode('utf-8')

f = open('html.txt','w',encoding="utf-8")
f.write(html)
f.close()
