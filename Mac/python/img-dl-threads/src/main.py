# ！ /usr/local/bin/python3
# _*_ coding:utf-8 _*_

from json import load as json_load
from os import mkdir as os_mkdir
from os.path import exists as os_path_exists
from queue import Queue
from random import choice as random_choice
from random import randint as random_randint
from random import shuffle as random_shuffle
from sys import path as sys_path
from threading import Thread as threading_Thread
from time import localtime as time_localtime
from time import sleep as time_sleep
from time import strftime as time_strftime

from requests import get as requests_get

from mylib.rest import Rest
from mylib.TextStatusBar import TextStatusBar

sys_path.append("/Users/linxi/Documents/python/")


class PageCrawl(threading_Thread):
    def __init__(self, name, pics_url, AUTHORS):
        super(PageCrawl, self).__init__()
        self.name = name
        self.pics_url = pics_url
        self.AUTHORS = AUTHORS
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        }
        # self.proxies = PageCrawl.getProxies(self)

    def run(self):
        print(self.name + " started.")
        rest = Rest()
        while len(self.pics_url) != 0:
            try:
                # {"name": key, "urls": page[key]}
                page = self.pics_url.pop()
                path = PageCrawl.makedir(self, page["name"])
                PageCrawl.img_dl(self, page["urls"], path)
            except:
                raise
            finally:
                rest.rest()

    def img_dl(self, urls, path):
        print(8)
        self.bar = TextStatusBar(len(urls))
        for url in urls:
            self.bar.show("img-dl: ")
            try:
                r = requests_get(url, headers=self.headers)
                r.raise_for_status
                with open(path + url.split("/")[-1], "rb") as f:
                    f.write(r.content)
            except:
                logger(url)

    def makedir(self, name):
        # name.replace(' ', '').replace('.', 'ß')
        a = True
        for author in self.AUTHORS:
            if author in name:
                path = "./img-dl-threads/Gitograms/" + author + "/" + name
                os_mkdir(path) if (not os_path_exists(path)) else True
                a = False
        if a:
            path = "./img-dl-threads/Gitograms/Others/" + name
            os_mkdir(path)
        return path

    def getProxies(self):
        proxies = []
        return proxies


def logger(message):
    date = time_strftime("[%Y-%m-%d %H:%M:%S]:", time_localtime())
    with open("./img-dl-threads/log.txt", "a+", encoding="utf-8") as f:
        f.write(date + message + "\n")


def createPageLock(start, end=0):
    with open("./img-dl-threads/pageLock", "w", encoding="utf-8") as f:
        a = []
        bar = TextStatusBar(abs(start - end) * 2)
        if start and not end:
            for i in range(1, start + 1):
                a.append(str(i))
                bar.show(indentation="Creating Lock: ")
        elif start and end:
            for i in range(start, end + 1):
                a.append(str(i))
                bar.show(indentation="Creating Lock: ")
        random_shuffle(a)
        for i in range(len(a)):
            f.write(a[i] + "\n")
            bar.show(indentation="Creating Lock: ")
        print()


def loadAuthor(path):
    with open(path, "r", encoding="utf-8") as f:
        authors = f.read().strip().split("\n")
    return authors


def getPage():
    RANGE = int(input("(range): "))
    print("DO NOT OPEN ANOTHER TERMINAL UNTIL...", end="")
    page = {}

    with open("./img-dl-threads/pageLock", "r", encoding="utf-8") as f:
        pageLock = f.read().strip().split("\n")

        for i in range(RANGE + 1):
            path = "./img-dl-threads/SaveData/page-" + pageLock.pop() + ".json"
            with open(path, "r", encoding="utf-8") as f:
                jstr = json_load(f)
            for key in jstr.keys():
                page[key] = jstr[key]

    with open("./img-dl-threads/pageLock", "w", encoding="utf-8") as f:
        f.write("\n".join(pageLock))
    print(" NOW. ")
    return page


def main():
    # createPageLock(367)
    AUTHORS = loadAuthor("./img-dl-threads/authors.txt")

    page = getPage()

    pics_url = []
    for key in page.keys():
        pics_url.append({"name": key, "urls": page[key]})

    pageCrawler = PageCrawl("crawler ", pics_url, AUTHORS)

    pageCrawler.run()

    print("pics_url is empty. ")


if __name__ == "__main__":
    main()
