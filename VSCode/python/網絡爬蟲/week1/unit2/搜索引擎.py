import requests


kv = {'wd':'鬼刀'}
agent = {'user-agent':"Mozilla/5.0"}
r = requests.get('https://www.baidu.com/s', params=kv, headers=agent)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.headers)