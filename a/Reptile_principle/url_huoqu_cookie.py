import http.cookiejar
import urllib.request

# cookie = http.cookiejar.CookieJar()
# hadle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(hadle)
# res = opener.open('https://www.baidu.com')
# for i in cookie:
#     print(i.name + '=',i.value)

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
hadle = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hadle)
res = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)