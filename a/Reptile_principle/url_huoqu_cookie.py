import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
hadle = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hadle)
res = opener.open('https://www.baidu.com')
print(res)