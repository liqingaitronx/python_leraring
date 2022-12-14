import urllib.request as url

res = url.urlopen('https://www.taobao.com',None,2 )

html = res.read().decode('utf-8')
# print(html)
f = open('html.txt','w',encoding='utf-8')
f.write(html)
f.close()
