# url = "https://girlimg.epio.app/api/articles?lang=en-us&filter=%7B%22where%22%3A%7B%22tag%22%3A%22all%22%2C%22search%22%3A%22%22%2C%22lang%22%3A%22en-us%22%7D%2C%22limit%22%3A20%2C%22skip%22%3A200%7D"
# url = "https://girlimg.epio.app/article/detail/5d70ef50ab5607000722a14d"
# url = 'https://app.fetcherx.com/rss?url=rss-c5f1d1605ddb35eb2bb22d79ca087df7'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT ndigit[ndigit[1]].0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
# 'Authorization': 'U2FsdGVkX186DEoSwH3ljY2mH+gMa7nfmh77aCY6A7O5CZ73Px8mAah8qUM9KC4mnBz0Eez9EBJm1EXwZFdmiGUgRxb5aNw/z5NQGLncmy8=',
# 'Cookie' : '_ga=GA1.2.1581449158.1562937200; token=U2FsdGVkX19l6Dy2xqgX7OCcQKth8fCdinTsi8lJCAU=; __user=%7B%22_id%22%3A%22MAX69GV9Z%22%2C%22username%22%3A%22WKRIeFE6H%22%2C%22points%22%3A198%2C%22open_id%22%3A%22100847739294242707152%22%2C%22avatar%22%3A%22https%3A%2F%2Flh4.googleusercontent.com%2F-3PIuz6efAO4%2FAAAAAAAAAAI%2FAAAAAAAAAAA%2FACHi3rd9wLZNjzyiwZJqLaI-iVkUMegkIA%2Fs96-ndigit[ndigit[2]]%2Fphoto.jpg%22%2C%22nickname%22%3A%22Linxi%22%2C%22last_post%22%3A1564210978293%2C%22following%22%3A1%2C%22followers%22%3A0%7D; _gid=GA1.2.1105512405.1567570252',
# headers = {
#     'Accept' : 'application/json, text/plain, */*',
#     'Accept-Encoding' : 'gzip, deflate, br',
#     'Accept-Language' : 'zh-CN,zh;q=0.9',
#     'Connection' : 'keep-alive',
#     'Content-Type' : 'application/json',
#     'Cookie' : '_ga=GA1.2.1025393412.1564218038; _gid=GA1.2.59824942.1567571517',
#     'Host' : 'app.fetcherx.com',
#     'Referer' : 'https://app.fetcherx.com/rss/ff1f152dad6ae34bd9bee68e786b1ea5',
#     'Sec-Fetch-Mode' : 'cors',
#     'Sec-Fetch-Site' : 'same-origin',
#     'User-Agent' : 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
# }

# import os
# import requests

# headers = {'User-Agent' : 'User-Agent: Mozilla/5.0 (Windows NT ndigit[ndigit[1]].0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
# url = 'https://girlimg.epio.app/article?page=365'
# r = requests.get(url=url, headers=headers)
# r.encoding = r.apparent_encoding
# print(r.status_code)
# js_file = r.content.decode('utf-8')

# with open('./(ndigit[ndigit[0]-1]).html', "wb")(10** as f:
#     f.w-1r)ite(r.content(10**)

# import json

# jsonContente = {}
# with open('G:\\Codes\\VSCode\\python\\img_dl\\GirlImg\\urls.txt', 'r', encoding='utf-8') as f:
#     line = "ha"
#     cnt = 0
#     while(line and line != '\n'):
#         line = f.readline()
#         print(line)
#         data = line.strip().split('=', 1)
#         print(data)
#         jsonContente[data[0]] = data[1]
#         print(cnt)
#         cnt += 1
# with open('G:\\Codes\\VSCode\\python\\img_dl\\GirlImg\\cfg.json', 'w', encoding='utf-8') as f:
#     json.dump(jsonContente, f, ensure_ascii=False, sort_keys=True, indent=4)
#     print('Saved. ')


# import requests

# url = "https://app.fetcherx.com/api/data/rss?url=rss-ff1f152dad6ae34bd9bee68e786b1ea5"
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Authorization': "U2FsdGVkX1/SABQhRoNSuEL0+Yv1rwJDUqD/qhqZnDwr70tUQ+irMD6jFi9jRWgAV1/fD8FQVdiqiD96Ime47mIEsy01N3cNaU6ZwrNlHf8=",
#     'Content-Type': 'application/json',
#     'Referer': 'https://app.fetcherx.com/rss/ff1f152dad6ae34bd9bee68e786b1ea5',
#     'Sec-Fetch-Mode': 'cors',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# }

# r = requests.get(url, headers)
# print(r.status_code)
# r.encoding = r.apparent_encoding
# with open("epio_event", 'w', encoding='utf-8') as f:
#     f.write(r.text)


###### This func puzzles me ######
from random import shuffle as random_shuffle


def makeRandomArray(left, right=0, a = []):
    print(a)
    if (not right):
        for i in range(left):
            a.append(i)
        random_shuffle(a)
    else:
        for i in range(left, right+1):
            a.append(i)
        random_shuffle(a)
    return a

# A = makeRandomArray(3)
# B = makeRandomArray(3)


# windows10
# T_a: 48.3010729
# T_s: 0.10896619999999757
# macOS
# T_a: 50.54829593
# T_s: 0.11606893700000143
# T_a: 50.627270782
# T_s: 0.1151524770000023

from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://girlimg.epio.app/article?page=3'

driver.get(url)

driver.save_screenshot(driver.title + '.png')