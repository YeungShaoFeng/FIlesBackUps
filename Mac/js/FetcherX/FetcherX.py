from execjs import get as execjs_get
from requests import get as requests_get
from json import dump as json_dump
from json import dumps as json_dumps
from json import load as json_load
from json import loads as json_loads
import time


class FetcherX:
    def __init__(self, startUrl, Range):
        self.F_Auth = "Auth()"
        self.JSFILE = "./Authrization.js"
        self.startUrl = startUrl
        self.Range = Range
        self.me = False
        self.headers = {
            "Host": "app.fetcherx.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "Sec-Fetch-Mode": "cors",
            "Content-Type": "application/json",
            "Sec-Fetch-Site": "same-origin",
            "Referer": "",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "_ga=GA1.2.1982932786.1569031957; _gid=GA1.2.1082012567.1571534857; _gat_gtag_UA_60788452_17=1",
        }
        node = execjs_get()
        with open(self.JSFILE, "r", encoding="utf-8") as f:
            self.ctx = node.compile(f.read())

    def loadJson(self, jsonPath=None, data=None):
        if jsonPath:
            with open(jsonPath, "r", encoding="utf-8") as f:
                json_string = json_load(f)
        elif data:
            if isinstance(data) == str:
                json_string = json_loads(data)
            else:
                json_string = json_load(dict(data))
        return json_string

    def saveJson(self, data, jsonPath):
        with open(jsonPath, "w", encoding="utf-8") as f:
            json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
        return None

    def getAuth(self):
        return self.ctx.eval(self.F_Auth)

    def getJSON(self, url):
        if self.me:
            FetcherX.getMe(self, url)
            self.me = False
        else:
            self.headers["Authorization"] = FetcherX.getAuth(self)
            try:
                r = requests_get(url=url, headers=self.headers)
                r.raise_for_status
                r.encoding = r.apparent_encoding
            except:
                raise
            finally:
                self.GitogramJson = FetcherX.loadJson(self, data=r.text)
                # --T
                FetcherX.saveJson(self, self.GitogramJson, "./GitogramJson.json")
                # --T

    def getMe(self, url):
        self.headers["Referer"] = url
        self.headers["Authorization"] = FetcherX.getAuth(self)
        try:
            r = requests_get(
                url="https://app.fetcherx.com/api/users/me", headers=self.headers
            )
            r.raise_for_status
            r.encoding = r.apparent_encoding
        except:
            raise
        finally:
            self.meJson = r.text
            #--T
            print(self.meJson)
            #--T
        return self.meJson

    def resolveRootJson(self):
        pass


fetcherx = FetcherX("", 1)
url = "https://app.fetcherx.com/user/5c9ab36e6dd5e80009d4deef"
fetcherx.getJSON(url)
