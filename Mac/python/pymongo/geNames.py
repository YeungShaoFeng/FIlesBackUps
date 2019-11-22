#! /usr/local/bin/python3
# _*_  coding:utf-8 _*_

from json import load as json_load
from main import TextStatusBar

def loadJson(jsonPath):
    with open(jsonPath, 'r', encoding='utf-8') as f:
        jstr = json_load(f)
    return jstr


def saveNames(num):
    names = []
    bar = TextStatusBar(num)

    for i in range(1, num+1):
        bar.show()
        jstr = loadJson('./SaveData/page-' + str(i) + '.json')
        for key in jstr.keys():
            names.append(key)

    with open('./names.txt', 'a+', encoding='utf-8') as f:
        for name in names:
            f.write(name + '\n')    

def main():
    # name = '[奈莉酱]帆风Lolita 画像48枚'
    names = []
    with open('./names.txt', 'r', encoding='utf-8') as f:
        name = f.readline().strip()
        while(name):
            names.append(name)
            name = f.readline().strip()            
    #  u'-',
    symbles = [u' ', u'《', u'自',
               u'，', u']', u'の',
               u'VOL', u'_N', u'－'
               u'無', u'--']
    # FA = open('./a.txt', 'w', encoding='utf-8')
    Fname = open('./name.txt', 'w', encoding='utf-8')
    for name in names:
        for symble in symbles:
            if(symble in name):
                name = name.split(symble)[0]
        if (u'[' in name):
            name = name.split(u'[')[1]
        Fname.write(name + '\n')

if __name__ == "__main__":
    main()