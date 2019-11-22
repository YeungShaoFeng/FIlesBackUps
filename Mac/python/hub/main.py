from requests import get as requests_get


url = 'https://www.pornhub.com/view_video.php?viewkey=ph5d15a48579700'

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


r = requests_get(url, headers=headers)

print(r.status_code)

r.encoding = r.apparent_encoding

with open('./pussy.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
