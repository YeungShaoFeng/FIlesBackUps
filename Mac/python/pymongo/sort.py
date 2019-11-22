#! /usr/local/bin/python3
# _*_ coding: utf-8 _*_

from json import load as json_load
from json import dump as json_dump
from os import listdir as os_listdir


class Sortor:
    def __init__(self, rawdir, RA, i):
        self.pageNums = Sortor.finder(self, rawdir, RA, i)

    def loadJson(self, jsonPath):
        with open(jsonPath, "r", encoding="utf-8") as f:
            json_string = json_load(f)
        return json_string

    def saveJson(self, data, jsonPath):
        with open(jsonPath, "w", encoding="utf-8") as f:
            json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
        return None

    def finder(self, rawdir, RA, i):
        # 获取目录列表
        allfile = os_listdir(rawdir)
        # 提取目录里已有的页数
        fileNum = []
        for file in allfile:
            if "page-" in file:
                fileNum.append(file[5:].split(".")[0])
        fileNum = sorted(fileNum)
        return fileNum

    def oOps(self, message, funcName):
        with open("./failed.txt", "a+", encoding="utf-8") as f:
            f.write(funcName + ":" + "\n")
            f.write(message + "\n")


def doSort():
    sortor = Sortor("./SaveData/", [], [1, 367])
    with open("./names.txt", "a+", encoding="utf-8") as f:
        try:
            for num in sortor.pageNums:
                jsonPath = "./SaveData/page-" + str(num) + ".json"
                jstr = sortor.loadJson(jsonPath)
                for key in jstr.keys():
                    f.write(key + "\n")
        except:
            sortor.oOps(key, "sort.py-main")

        finally:
            print("All Done.")

# def main():
#     with open('./author.json', 'r', encoding='utf-8') as f:
#         jstr = json_load(f)
#     with open('./author.txt', 'a+', encoding='utf-8') as f:
#         for title in jstr['items']:
#             print(title['title'])
#             f.write(title['title'] + '\n')


if __name__ == "__main__":
    doSort()