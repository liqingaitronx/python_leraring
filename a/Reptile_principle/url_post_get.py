import requests
# url = 'http://httpbin.org/post'
# data = {'name':'james','age':18}
# re = requests.post(url,data = data)
# print(re.text)    #pos


url  = 'http://httpbin.org/get'
data ={'name':'niede','age':22}
res = requests.get(url,data=data)
print(res.text)
print(type(res))
print(res.status_code)
print(res.cookies)
print(res.json())