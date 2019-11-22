from json import dump as json_dump
from json import dumps as json_dumps
from json import load as json_load
from json import loads as json_loads
from queue import Queue
from time import time as t_time


def loadJson(data=None, jsonPath=None):
    json_string = {}
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


def saveJson(data, jsonPath):
    try:
        with open(jsonPath, "w", encoding="utf-8") as f:
            json_dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
    except:
        print("BUG: saveJson")
        return False
    finally:
        return True


def a():
    jsonPath = "./url/girlimg.json"
    a = loadJson(jsonPath=jsonPath)
    for i in range(len(a["userFolders"])):
        print(i)
        a["userFolders"][i]["localPath"] = (
            "./img/bookmarks/girlimg/" + a["userFolders"][i]["localPath"][9:]
        )
    saveJson(a, "./url/bookmarks/girlimg.json")


# from mylib.textStatusBar import TextStatusBar as TSB
# from time import sleep as t_sleep
# a, b = 10, 20
# bar1 = TSB(a)
# bar2 = TSB(b)


# for i in range(a):
#     bar1.hide()
#     for j in range(b):
#         t_sleep(0.5)
#         bar2.show(indentation=bar1.refresh())
#     bar2.clear()

# import os
# rows, columns = os.popen('stty size', 'r').read().split()
# print((rows, columns))
# def dada(b):
#     return ['1', b if b else 'None']
# print(dada(1))


a = [x for x in range(10)]
myQueue = Queue(len(a))
for x in a:
    myQueue.put(x)


def dada(myQueue):
    data = []
    for var in myQueue:
        data.append(var)
    # for i in range(myQueue.qsize()):
    #     data.append(myQueue.get())
    return data


print(dada(myQueue))
