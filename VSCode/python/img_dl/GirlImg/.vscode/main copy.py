# -*- coding:utf-8 -*-

import os
import json
import time
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TextStatusBar import TextStatusBar


def pic_sets_url_locator(driver, pic_sets_url_xpath):
    # 获取一组包含有图集链接的元素
    # pic_sets_urls = driver.find_elements_by_xpath(pic_sets_url_xpath)
    pic_sets_urls = driverWaitUntilXpath(
        driver, pic_sets_url_xpath, 'pic_sets')
    # 遍歷提取链接
    for i in range(len(pic_sets_urls)):
        pic_sets_urls[i] = pic_sets_urls[i].get_attribute('href')
    return pic_sets_urls


def img_dl(driver, headers, title, pics_url, picSets_dir='.'):
    # 合成保存路径
    route = picSets_dir + '/' + title.replace(" ", "")
    # 進度條
    bar = TextStatusBar(len(pics_url))

    print("Saving: \"{}\" ".format(title))

    # 判斷圖集文件夾是否存在
    if (not os.path.exists(route)):
        os.mkdir(route)
    else:
        print("{} already exits.".format(route))

    cnt = 0  # 图片计数器
    for i in range(len(pics_url)):
        cnt += 1
        # 圖片進程
        bar.show()
        # 下载图片
        r = requests.get(pics_url[i], headers)
        if(r.status_code != 200):
            print("No.{} GET falied. Status_code:{}".format(cnt, r.status_code))
            continue
        # 保存图片
        with open(route + "/{}.jpg".format(cnt), "wb") as f:
            f.write(r.content)
        # 避免圖集名和進程冲突
        print() if (i == len(pics_url-1)) else True

# The driver will wait until it finds out all the elements by XPath


def driverWaitUntilXpath(driver, xpath, mode=''):
    try:
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except:
        # 遞歸等待所有元素被找到
        elements = driverWaitUntilXpath(driver, xpath, mode)
    finally:
        if ('pic_sets' in mode):
            elements = elements[:20]
        elif('title' in mode):
            elements = elements[0]
        else:
            elements = elements

        return elements


def saveDataAsJson(data, jsonPath):
    print("Saving... ", end='')
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
    print('Done. ')


def spider(driver, cfg):
    # 以頁爲單位進行爬取
    for i in range(1, 3):
        page = str(i)
        # 獲取第 i 頁
        driver.get(base_url.format(i))
        # 下拉到底部
        driver.execute_script(scrollToBottom)
        driver.save_screenshot('./epio.png')
        print("$PAGE: " + page)
        # 提取當前網頁的20個圖集鏈接
        # 每一頁都是20個圖集
        print("{}Locating All Gitograms...".format(indentations["eins"]), end='')
        pic_sets_urls = pic_sets_url_locator(
            driver, pic_sets_url_xpath)
        print("Done. ")
        # 去掉第一頁的第一個個RSS urls
        if (i == 1):
            pic_sets_urls = pic_sets_urls[1:]
        # 遍历下载
        for pic_sets_url in pic_sets_urls:
            # 轉到圖集頁
            print("{}Getting \"{}\"... ".format(indentations["zwei"], pic_sets_url), end='')
            driver.get(pic_sets_url)
            driver.save_screenshot('./epio.png')
            print("Done. ")
            # 獲取圖集標題
            print("{}Extrancting tilte... ".format(indentations["zwei"]), end='')
            title = driverWaitUntilXpath(driver, title_xpath, 'title').text
            print("Done. ")
            # 輸出目標名稱
            print("{}Target title: {}".format(indentations["zwei"], title))
            # 獲取每一張圖片的元素對象
            print("{}Extrancting pics_url elements...".format(indentations["zwei"]), end='')
            pics_url = driverWaitUntilXpath(driver, pics_url_xpath)
            print("Done. ")
            bar = TextStatusBar(len(pics_url))
            # 遍歷提取每張圖片的url
            print("{}Extrancting pics_url...".format(indentations["zwei"]))
            for i in range(len(pics_url)):
                pics_url[i] = pics_url[i].get_attribute("src")
                bar.show(indentations['zwei'])
            print("\n{} Done. ".format(indentations["zwei"]))
            # # 下載圖集
            # img_dl(driver, headers, title, pics_url, picSets_dir)
            print("{}Adding pics_url to pic_urlsData... ".format(indentations["zwei"]), end='')
            pic_urlsData[title] = pics_url
            print("Done. ")
        pic_setsData[page] = pic_urlsData
        # 清空 pic_urlsData 來寫入下一組數據
        pic_urlsData = {}
    saveDataAsJson(pic_setsData, jsonPath)    


def main():
    t1 = time.perf_counter()

    cfgRoute = './cfg.json'
    with open(cfgRoute, 'r', encoding='utf-8') as fp:
        cfg = json.load(fp)
    
    options = webdriver.ChromeOptions()
    # 無頭模式
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("user-data-dir=" + os.path.abspath(cfg["profile_dir"]))
    # disable the DevTools Logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    spider(driver, cfg)

    t2 = time.perf_counter()
    T = t2 - t1
    print("Total time: {}s,\t{}m.".format(T, T/60))
    print("Ave: {}s,\t{}m.".format(T/20, T/1200))


if __name__ == "__main__":
    main()
