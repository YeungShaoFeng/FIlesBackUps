import requests


url = 'https://www.python123.com'
r = requests.get(url)
if (r.status_code == 200):
    r.encoding = r.apparent_encoding
    print(r.headers)
    print(r.apparent_encoding)
    print(r.text)
    print(r.content)
else:
    print("Something went wrong!")

