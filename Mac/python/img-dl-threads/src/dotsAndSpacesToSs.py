#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

from json import dump as json_dump
from json import load as json_load
from sys import path as sys_path
sys_path.append("/Users/linxi/Documents/python/")
from mylib.TextStatusBar import TextStatusBar

def loadJson(jsonPath):
    with open(jsonPath, "r", encoding="utf-8") as f:
        json_string = json_load(f)
    return json_string


def saveJson(data, jsonPath):
    with open(jsonPath, "w", encoding="utf-8") as f:
        json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
    return None


def dotsAndSpacesToSs(pageNum):
    bar = TextStatusBar(pageNum)
    for i in range(1, pageNum + 1):
        bar.show()
        jsonPath = "./SaveData/page-" + str(i) + ".json"
        jstr = loadJson(jsonPath)
        newJstr = {}
        Ss, dot, space = "ß", ".", " "
        for key in jstr.keys():
            newKey = key.replace(dot, Ss).replace(space, Ss)
            newJstr[newKey] = jstr[key]
        saveJson(newJstr, jsonPath)
    print()

def main():
    dotsAndSpacesToSs(367)

if __name__ == "__main__":
    main()