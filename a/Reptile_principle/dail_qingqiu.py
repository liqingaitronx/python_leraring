from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxyhad = ProxyHandler({
    'https':"183.245.6.16:8080"
})#设置请求代理


opner = build_opener(proxyhad)
try:
    resp = opner.open("https://www.taobao.com/")
    print(resp.read().decode('utf-8'))
except URLError as e:
    print(e.reason)