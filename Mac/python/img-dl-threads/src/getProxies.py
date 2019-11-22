#! /usr/local/bin/python3
# _*_ conding:utf-8 _*_

from requests import get as requests_get
from bs4 import BeautifulSoup
from sys import path as sys_path
sys_path.append("/Users/linxi/Documents/python/")
from mylib.TextStatusBar import TextStatusBar


class GetProxies:
    def __init__(self, urls, headers=False):
        self.urls = urls
        self.proxies = {}
        if headers:
            self.headers = headers
        else:
            self.headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
            }

    def get(self):
        for url in self.urls:
            if "xicidaili.com" in url:
                self.proxies["xicidaili"] = {}
                GetProxies.xicidaili(self, url)

    def xicidaili(self, url):
        self.proxies["xicidaili"] = {}
        try:
            r = requests_get(url=url, headers=self.headers)
            r.raise_for_status
            r.encoding = r.apparent_encoding

            soup = BeautifulSoup(r.text, "lxml")
            tds = soup.find_all("td")

            self.bar = TextStatusBar(len(tds) // 10)
            for i in range(len(tds) // 10):
                self.bar.show()
                i_10 = i * 10
                ip = tds[i_10 + 1].string
                port = tds[i_10 + 2].string
                if ip and port:
                    self.proxies["xicidaili"][str(i)] = {
                        "http": "http://" + ip + ":" + port,
                        "https": "https://" + ip + ":" + port,
                    }
        except:
            pass
        GetProxies.test(self, 'xicidaili')

    def test(self, domain):
        self.bar = TextStatusBar(len(self.proxies[domain]))
        bads, proxies = [], {}
        # for i in range(len(self.proxies[domain])):
        #     proxies[i] = self.proxies[domain][i]
        # self.proxies[domain] = proxies
        for key in list(self.proxies[domain].keys()):
            self.bar.show(indentation="Testing: ")
            try:
                proxy = self.proxies[domain][key]
                r = requests_get("https://bing.com", proxies=proxy, timeout=1)
                if (r.status_code != 200):
                    bads.append(key)
            except:
                bads.append(key)
        for bad in bads:
            del self.proxies[domain][bad]
        print()


urls = ["https://www.xicidaili.com/nn/1"]
porxy = GetProxies(urls)
porxy.get()
print(len(porxy.proxies))
