import os
import requests


url = 'https://cdn1-images.epio.app/image/download/aHR0cDovL2NkbnYyLmdpcmxpbWcuY29tL2ltYWdlcy9Gc09neHB4LUhlcE4yYzdkUWc4OHl1OTJNMy11'
agent = {'user-agent':'Mozilla/5.0'}
root = 'G:\\img-vdo\\'
path = root + url.split('/')[-1] + '.jpg'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url, headers=agent)
        r.encoding = r.apparent_encoding
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("Tin~")
    else:
        print("文件已存在。")
except:
    print("爬取失敗。")
    raise