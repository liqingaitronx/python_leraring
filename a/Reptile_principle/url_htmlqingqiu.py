import pandas as pd
import requests
import re

url = 'https://tophub.today/n/Jb0vmloB1G'
headers = {
'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
r = requests.get(url=url,headers=headers).text
# print(r)
title = re.compile('itemid="[0-9]*">(.*?)</a>')
titles = title.findall(r)[0:30]
num = re.compile('<td>(.*?)</td>')
nums = num.findall(r)[0:30]
# print(titles)
m = {'今日热点':titles,'     热度':nums}
file = pd.DataFrame(m)
print(file)