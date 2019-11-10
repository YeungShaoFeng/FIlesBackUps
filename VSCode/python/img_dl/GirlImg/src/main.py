# -*- coding:utf-8 -*-

from json import dump as json_dump
from json import load as json_load
from os import mkdir as os_mkdir
from os.path import abspath as os_path_abspath
from os.path import exists as os_path_exists
from queue import Queue
from random import choice as random_choice
from random import randint as random_randint
from random import shuffle as random_shuffle
from re import compile as re_compile
from re import findall as re_findall
from requests import get as requests_get
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit as sys_exit
from time import localtime as time_localtime
from time import perf_counter as time_perf
from time import strftime as time_strf
from time import sleep as time_sleep

from TextStatusBar import TextStatusBar


def pic_sets_url_locator(driver, pic_sets_url_xpath):
    # 获取一组包含有图集链接的元素
    pic_sets_urls = driverWaitUntilXpath(driver, pic_sets_url_xpath, "pic_sets")
    # 遍歷提取链接
    for i in range(len(pic_sets_urls)):
        pic_sets_urls[i] = pic_sets_urls[i].get_attribute("href")
    return pic_sets_urls


def img_dl(driver, headers, title, pics_url, picSets_dir="."):
    # 合成保存路径
    route = picSets_dir + "/" + title.replace(" ", "")
    # 進度條
    bar = TextStatusBar(len(pics_url))

    print('Saving: "{}" '.format(title))

    # 判斷圖集文件夾是否存在
    if not os_path_exists(route):
        os_mkdir(route)
    else:
        print("{} already exits.".format(route))

    cnt = 0  # 图片计数器
    for i in range(len(pics_url)):
        cnt += 1
        # 圖片進程
        bar.show()
        # 下载图片
        r = requests_get(pics_url[i], headers)
        if r.status_code != 200:
            print("No.{} GET falied. Status_code:{}".format(cnt, r.status_code))
            continue
        # 保存图片
        with open(route + "/{}.jpg".format(cnt), "wb") as f:
            f.write(r.content)
        # 避免圖集名和進程冲突
        print() if (i == len(pics_url - 1)) else True


# The driver will wait until it finds out all the elements by XPath
def driverWaitUntilXpath(driver, xpath, mode=""):
    try:
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except:
        # 遞歸等待所有元素被找到
        elements = driverWaitUntilXpath(driver, xpath, mode)
    finally:
        if "pic_sets" in mode:
            elements = elements[:20]
        elif "title" in mode:
            elements = elements[0]
        else:
            elements = elements

        return elements


# snap a little bit
# 0.3 -- 3.6
def rest():
    snap = [random_randint(1, 3), random_randint(1, 3), random_randint(1, 3)]
    ndigit = [random_randint(1, 3), random_randint(1, 3), random_randint(1, 3)]
    random_shuffle(ndigit)
    choice = random_choice([0, 1, 2, 3, 4, 5])
    if choice == 0:
        snap = (
            snap[0] / (ndigit[ndigit[0] - 1])
            + snap[1] / (10 ** ndigit[ndigit[1] - 1])
            + snap[2] / (10 ** ndigit[ndigit[2] - 1])
        )
    elif choice == 1:
        snap = (
            snap[0] / (ndigit[ndigit[0] - 1])
            + snap[2] / (10 ** ndigit[ndigit[1] - 1])
            + snap[1] / (10 ** ndigit[ndigit[2] - 1])
        )
    elif choice == 2:
        snap = (
            snap[1] / (ndigit[ndigit[0] - 1])
            + snap[0] / (10 ** ndigit[ndigit[1] - 1])
            + snap[2] / (10 ** ndigit[ndigit[2] - 1])
        )
    elif choice == 3:
        snap = (
            snap[1] / (ndigit[ndigit[0] - 1])
            + snap[2] / (10 ** ndigit[ndigit[1] - 1])
            + snap[0] / (10 ** ndigit[ndigit[2] - 1])
        )
    elif choice == 4:
        snap = (
            snap[2] / (ndigit[ndigit[0] - 1])
            + snap[0] / (10 ** ndigit[ndigit[1] - 1])
            + snap[1] / (10 ** ndigit[ndigit[2] - 1])
        )
    elif choice == 5:
        snap = (
            snap[0] / (ndigit[ndigit[0] - 1])
            + snap[1] / (10 ** ndigit[ndigit[1] - 1])
            + snap[0] / (10 ** ndigit[ndigit[2] - 1])
        )
    snap = round(snap, ndigit[choice % 3])

    time_sleep(snap)


def saveDataAsJson(data, jsonPath, i):
    os_mkdir(jsonPath) if (not os_path_exists(jsonPath)) else True
    jsonPath += "/page-{}.json".format(i)
    print("Saving data to '{}'... ".format(jsonPath), end="")
    with open(jsonPath, "w", encoding="utf-8") as f:
        json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
    print("Done. ")


def girlimgSpider(driver, cfg, pageNum):
    pic_urlsData = {}
    # 獲取第 i 頁
    driver.get(cfg["base_url"].format(pageNum))
    # 下拉到底部
    driver.execute_script(cfg["scrollToBottom"])
    driver.save_screenshot("./epio.png")
    # 提取當前網頁的20個圖集鏈接(每一頁都是20個圖集)
    print("\n{}Locating All Gitograms...".format(cfg["indentations"]["eins"]), end="")
    pic_sets_urls = pic_sets_url_locator(driver, cfg["pic_sets_url_xpath"])
    print("Done. ", end="")
    # 去掉第一頁的第一個個 RSS urls
    if pageNum == 1:
        pic_sets_urls = pic_sets_urls[1:]

    random_shuffle(pic_sets_urls)

    while len(pic_sets_urls) != 0:
        pics_set_url = pic_sets_urls.pop()
        # 轉到圖集頁
        driver.get(pics_set_url)
        # 下拉到底部
        driver.execute_script(cfg["scrollToBottom"])
        rest()
        driver.save_screenshot("./epio.png")
        # 獲取圖集標題
        title = driverWaitUntilXpath(driver, cfg["title_xpath"], "title").text
        # 輸出目標名稱
        print("\n{}Target title: {}".format(cfg["indentations"]["zwei"], title), end="")
        # # 獲取每一張圖片的元素對象
        pics_url = driverWaitUntilXpath(driver, cfg["pics_url_xpath"])
        bar = TextStatusBar(len(pics_url))
        # 遍歷提取每張圖片的url
        print("\n{}Extrancting pics_url...".format(cfg["indentations"]["zwei"]))
        for i in range(len(pics_url)):
            pics_url[i] = pics_url[i].get_attribute("src")
            bar.show(cfg["indentations"]["zwei"])

        print(
            "\n{}Adding pics_url to pic_urlsData... ".format(
                cfg["indentations"]["zwei"]
            ),
            end="",
        )
        pic_urlsData[title] = pics_url
        print("Done. ")
    return pic_urlsData


# Only returns when the first num is bigger than the second one.
# @return [int, int]
def getInput():
    def exit0():
        print("Something wrong with your input. ")
        sys_exit(0)

    def check():
        yesorno = input("Are you sure?[(y)|n]").strip()
        if (not yesorno) or ("y" in yesorno):
            yesorno = True
        elif "n" in yesorno:
            yesorno = False
        else:
            exit0()
        return yesorno

    a = input(
        u"->!!!不能從 0 開始!!!<-\n->!!!輸入[1,366]以内的數字!!!<-\n[startPage,endPage]: "
    ).strip()
    if check():
        pattern = re_compile(r"[0-9]{1,3}")
        match = re_findall(pattern, a)
        if len(match) == 2:
            match[0], match[1] = int(match[0]), int(match[1])
            exit0() if (not match[0]) else True
            return match if (match[1] - match[0] > 0) else exit0()
        else:
            exit0()
    else:
        task = getInput()
        return task


# if right was specified, it returns a random array in range(left, right+1).
# else it returns an random array in range(0, left).
# @return [int...]
def makeRandomArray(left, right=0):
    a = []
    if not right:
        for i in range(left):
            a.append(i)
        random_shuffle(a)
    else:
        for i in range(left, right + 1):
            a.append(i)
        random_shuffle(a)
    return a


def getDriver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        # 無頭模式
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    # disable the DevTools Logs
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    return driver


def loadCfg(cfgRoute):
    try:
        with open(cfgRoute, "r", encoding="utf-8") as fp:
            cfg = json_load(fp)
    except:
        print("Somethig wrong with the cfg file.")
        sys_exit(1)
    return cfg


def main():
    # get task input from user
    task = getInput()

    # load the cfg file
    cfgRoute = "./cfg.json"
    cfg = loadCfg(cfgRoute)

    # initialize the webdriver as Chrome
    driver = getDriver()

    # make a random list of nums
    RA1 = makeRandomArray(task[0], task[1])

    t1 = time_perf()
    while len(RA1) != 0:
        # contianer for the json file
        Gitograms = {}

        i = RA1.pop()
        # 以頁爲單位進行爬取
        page = str(i)
        print("{}PAGE: ".format(cfg["indentations"]["eins"]) + page, end="")
        Gitograms = girlimgSpider(driver, cfg, i)
        saveDataAsJson(Gitograms, cfg["URLSSAVINGPATH"], i)
    t2 = time_perf()

    T = t2 - t1
    print("Total time: {}s,\t{}m.".format(T, T / 60))
    print("Ave: {}s,\t{}m.".format(T / 20, T / 1200))


if __name__ == "__main__":
    main()
