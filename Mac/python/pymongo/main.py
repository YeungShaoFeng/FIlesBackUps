# _*_ coding: utf-8 _*_
#! /usr/bin/python3

import pymongo
from sys import exit as sys_exit
from json import load as json_load
from json import dump as json_dump


class TextStatusBar:
    def __init__(self, scale):
        self.scale = scale
        self.length = 60
        self.cnt = 0

    def show(self, onlyOpercets=False, indentation=""):
        self.cnt += 1
        percents = self.cnt / self.scale
        pound = int(percents * self.length)
        space = int(self.length - pound)
        a = "#" * pound
        b = " " * space
        c = (self.cnt / self.scale) * 100
        if indentation != "":
            if onlyOpercets:
                print("{:^3.0f}%".format(c), end="")
            else:
                print("\r{}[{}{}] {:^3.0f}%".format(indentation, a, b, c), end="")
        else:
            print("\r[{}{}] {:^3.0f}%".format(a, b, c), end="")


class MongoGo:
    def __init__(self, db, collection):
        self.collection = MongoGo.mongoGo(self, db, collection)
        self.jsonPath = ""

    def setJsonPath(self, jsonPath):
        self.jsonPath = jsonPath

    def mongoGo(self, db, collection):
        # 链接 mongodb
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        # 检查 db 是否存在
        dblist = myClient.list_database_names()
        if db in dblist:
            print("DB exsits.")
            mydb = myClient[db]
        else:
            sys_exit(1)

        # 检查 collection 是否存在
        collist = mydb.list_collection_names()
        if collection in collist:
            print("col exsits.")
        else:
            sys_exit(2)
        # return collection
        return mydb[collection]

    def loadJson(self, jsonPath):
        with open(jsonPath, "r", encoding="utf-8") as f:
            json_string = json_load(f)
        return json_string

    def saveJson(self, data, jsonPath):
        with open(jsonPath, "w", encoding="utf-8") as f:
            json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
        return None

    def dotsAndSpacesToSs(self, pageNum):
        for i in range(1, pageNum + 1):
            print(i, end="...")
            jsonPath = "./SaveData/page-" + str(i) + ".json"
            jstr = MongoGo.loadJson(self, jsonPath)
            newJstr = {}
            Ss, dot, space = "ß", ".", " "
            for key in jstr.keys():
                newKey = key.replace(dot, Ss).replace(space, Ss)
                newJstr[newKey] = jstr[key]
            MongoGo.saveJson(self, newJstr, jsonPath)
            print("Done. ")

    def mongoInsertor(self, data, onceAtime=False):
        try:
            if onceAtime:
                cnt = 0
                for var in zip(data.keys(), data.values()):
                    a = {}
                    a['author'], a['urls'] = var[0], var[1]
                    self.collection.insert_one(a)
                    cnt += 1
        except:
            MongoGo.oOps(self, a)
        finally:
            return cnt

    def oOps(self, message):
        with open("./failed.txt", "a+", encoding="utf-8") as f:
            f.write(message)
            f.write("\n")


def insertUrlsToMongo():
    myMongo = MongoGo("girlimg", "gitograms")
    bar = TextStatusBar(367)

    for i in range(1, 368):
        bar.show()
        jsonPath = "./SaveData/page-" + str(i) + ".json"
        jstr = myMongo.loadJson(jsonPath)
        a = myMongo.mongoInsertor(jstr, onceAtime=True)
        print("Inserted " + str(a) + " gitogram urls.", end='')
    print()

def main():
    names = []
    ALL = []
    gitograms = {}

    with open('./author.txt', 'r', encoding='utf-8') as f:
        name = f.readline().strip()
        names.append(name)

    for i in range(368):
        page = './SaveData/page-' + str(i) + '.json'
        with open(page, 'r', encoding='utf-8') as f:
            jstr = json_load(f)

        for pics_set in jstr:
            for name in names:
                if (name in pics_set):
                    pass
if __name__ == "__main__":
    main()
