import io
import sys
import requests


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = 'https://girlimg.epio.app/article?page=1&tab=%E4%B8%AD%E5%9B%BD'
kv = {'user_agent':'Mozilla/5.0'}
r = requests.get(url, headers=kv)

print(r.status_code)
r.encoding = r.apparent_encoding
with open('./girlimg.html', 'w') as f:
    f.write(r.text)
print('good') 