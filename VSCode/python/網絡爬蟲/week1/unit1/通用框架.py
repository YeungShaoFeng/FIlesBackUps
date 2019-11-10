import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() # 如果狀態碼不是200，引發HTTPError異常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something went wrong!"


if __name__ == "__main__":
    url = "https://www.baidu.com"
    print(getHTMLText(url))