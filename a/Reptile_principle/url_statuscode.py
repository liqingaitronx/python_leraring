import  requests

url =  'https://taobao.com/'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
re = requests.get(url,headers=headers)
print(re.status_code)
print(re.cookies)
print(re.headers)
print(re.url)
print(re.history)
exit() if not re.status_code == requests.codes.ok else print("Request ok ")