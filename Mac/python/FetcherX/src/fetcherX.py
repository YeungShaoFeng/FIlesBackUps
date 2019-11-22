from json import dump as json_dump
from json import dumps as json_dumps
from json import load as json_load
from json import loads as json_loads
from sys import path as sys_path
from time import time as t_time

from execjs import get as execjs_get
from requests import get as requests_get

from mylib.textStatusBar import TextStatusBar as TSB

sys_path.append("/Users/linxi/Documents/python/")

D = "https://app.fetcherx.com/"
A = "api/"
F = "folder/"
DF = D + F
DA = D + A
DAF = DA + F
DAFFt = DAF + "folder_tags/"
DAFBu = DAF + "byUser/"


def timeStamp():
    return str(int(t_time() * 1000))


def get(url, img=True):
    try:
        r = requests_get(
            url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
            },
        )
        r.raise_for_status
        r.encoding = r.apparent_encoding
    except:
        raise
    return r.content if img else r.text


class FetcherX:
    def __init__(self, userUrl):
        self.F_Auth = "Auth()"
        self.JSFILE = "./FetcherX/src/Authrization.js"
        self.userUrl = userUrl
        self.user_id = userUrl.split("/")[-1]
        self.noReferer = True
        self.referer = ""
        self.userFolder_json = {}
        node = execjs_get()
        with open(self.JSFILE, "r", encoding="utf-8") as f:
            self.ctx = node.compile(f.read())
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

    def loadJson(self, data=None, jsonPath=None):
        try:
            if jsonPath:
                with open(jsonPath, "r", encoding="utf-8") as f:
                    json_string = json_loads(f.read())
            elif data:
                if isinstance(data, str):
                    json_string = json_loads(data)
                elif isinstance(data, dict):
                    json_string = json_load(dict(data))
        except:
            print("BUG: loadJson")
            return False
        finally:
            return json_string

    def saveJson(self, data, jsonPath):
        try:
            with open(jsonPath, "w", encoding="utf-8") as f:
                json_dump(data, f, ensure_ascii=False,
                          sort_keys=True, indent=4)
        except:
            print("BUG: saveJson")
            return False
        finally:
            return True

    def getAuth(self):
        return self.ctx.eval(self.F_Auth)

    def GET(self, url, content=False, referer=None, noreferer=False):
        if noreferer:
            self.noReferer = noreferer
        if self.noReferer:
            self.headers["Referer"] = self.userUrl
            self.noReferer = False
        elif referer:
            self.headers["Referer"] = referer
            self.noReferer = False
        self.headers["Authorization"] = FetcherX.getAuth(self)
        try:
            r = requests_get(url=url, headers=self.headers)
            r.raise_for_status
            r.encoding = r.apparent_encoding
        except:
            raise
        return r.content if content else r.text

    def GETMe(self):
        self.noReferer = False
        return FetcherX.GET(self, url=DA + "users/me")

    def getTagFromJson(self, data, urlKey):
        a = FetcherX.loadJson(self, data=data)
        lista = []
        for var in a:
            lista.append(var[urlKey])
        return lista

    def setReferer(self, referer):
        self.headers["Referer"] = referer
        self.noReferer = False

    def getUserInfo(self, willSave):
        self.setReferer(self.userUrl)
        self.username = self.loadJson(
            data=self.GET(DA + "users/getByUserId/" + self.user_id)
        )["username"]
        if willSave:
            self.userFolder_json = self.GET(
                DA + "folder/byUser/" + self.user_id)
            self.saveJson(
                self.loadJson(self.userFolder_json), "./" +
                self.user_id + ".json"
            )
        self.GET(
            DA + "users/followList?type=followers&user_id=" + self.user_id + "&page=0"
        )
        self.GET(
            DA + "users/followList?type=following&user_id=" + self.user_id + "&page=0"
        )
        self.GET(DA + "users/isFollow/" + self.user_id)

    def getUrlsFromUserFolders(self):
        userFoldesrInfo = {
            "userId": self.user_id,
            "localPath": "./" + self.username,
            "userFolders": [],
        }
        folder_ids = self.getTagFromJson(self.userFolder_json, "_id")
        folderNames = self.getTagFromJson(self.userFolder_json, "name")
        folderCounts = self.getTagFromJson(self.userFolder_json, "count")
        print("Getting " + self.username + " infos...")

        for folder_id, folderName, folderCount in zip(
            folder_ids, folderNames, folderCounts
        ):
            urls = []
            self.setReferer(DF + folder_id)

            self.GET(DAF + "getUserByFolderId/" + folder_id)
            urls.append(
                self.getTagFromJson(
                    self.GET(DAF + folder_id + "?last=0"), "url")
            )
            self.GET(DAFFt + folderName)
            self.GET(DAFBu + self.user_id)

            bar = TSB(int(folderCount) // 20 + 1)
            for i in range(int(folderCount) // 20 + 1):
                bar.show()
                urls.append(
                    self.getTagFromJson(
                        self.GET(DAF + folder_id + "?last=" +
                                 timeStamp()), "url"
                    )
                )
            userFoldesrInfo["userFolders"].append(
                {
                    "name": folderName,
                    "localPath": userFoldesrInfo["localPath"] + folderName,
                    "count": folderCount,
                    "urls": urls,
                }
            )
            self.GETMe()
        return userFoldesrInfo


def main():
    url = "https://app.fetcherx.com/user/5c9ab36e6dd5e80009d4deef"
    fx = FetcherX(url)
    # fx.GETMe()
    fx.getUserInfo(willSave=True)
    userFoldersInfo = fx.getUrlsFromUserFolders()
    fx.saveJson(userFoldersInfo, "./FetcherX/url/bookmarks/" +
                fx.username + ".json")


main()
