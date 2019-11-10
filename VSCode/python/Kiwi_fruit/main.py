# _*_ encoding:utf-8 _*_

import re
import time


class Kiwi:

    DATE = time.strftime("%Y-%m-%d", time.localtime())

    def __init__(self, Time, case, weight):
        self.Time = Time
        self.case = case
        self.weight = weight
        self.cnt = 0
        self.sumOfCases = 0
        self.sumOfWeight = 0.0
        self.FILEROUTE = time.strftime("./data%H_%M_%S.csv", time.localtime())

    def set(self, case, weight):
        self.case = case
        self.weight = weight

    def writer(self, isFirstLine):
        def sum_writer():
            self.cnt += 1
            self.sumOfCases += int(self.case)
            self.sumOfWeight += int(self.weight)
        if (isFirstLine):
            with open(self.FILEROUTE, 'w', encoding='utf-8') as f:
                f.write(u"次數,箱數,重量/kg,時間\n")
        if (not isFirstLine):
            self.Time = time.strftime("%H:%M:%S", time.localtime())
            with open(self.FILEROUTE, "a+") as f:
                sum_writer()
                sentence = '{},{},{},{}\n'.format(str(self.cnt), str(self.case), str(self.weight), str(self.Time))
                f.write(sentence)

    def showData(self):
        with open(self.FILEROUTE, 'r', encoding='utf-8') as f:
            line = f.readline().strip().split(',')
            line = '{}   {}   {}   {}'.format(line[0],line[1],line[2],line[3])
            print(line)
            line = f.readline().strip()
            while(line):
                print(' ' + line.replace(',', '\t'))
                line = f.readline().strip()

    def summup(self):
        print(u"\n總計：{} 箱. ".format(self.sumOfCases))
        print(u"總重：{} KG({} HKG). \n".format(self.sumOfWeight/2, self.sumOfWeight))

    def sort(self):
        pass


# global kiwi
kiwi = Kiwi(0, 0, 0)
kiwi.writer(True)


def pmt(words):
    def subPmt():
        print("Default input data type is two numerical\ndata seperated with a comma inside. ")
        print(">\'show\'{}Show Datas".format(" " * 8))
        print(">\'sum\'{}Sum up'".format(" " * 9))
        print(">\'help\'{}Show helps".format(" " * 8))

    print(words) if (words) else subPmt()


def whatToDo(opt):
    if ("show" in opt):
        kiwi.showData()

    elif("sum" in opt):
        kiwi.summup()

    elif("help" in opt):
        pmt('')

    elif(len(opt) == 2):
        kiwi.set(opt[0], opt[1])
        kiwi.writer(False)

    else:
        print("Something wrong with your input. ")


def getOpt(isFirst):
    pmt(True) if isFirst else 1
    opt = input(":")
    if (len(opt.split(',')) == 2):
        opt = check(opt)
    return opt


def check(_input):
    new_input = _input.split(',')
    pattern = r'\d'

    for i in range(2):
        match = re.findall(pattern, new_input[i])
        lenOf_match = len(match)
        if (not i):
            if (lenOf_match == 1):
                continue
            else:
                break

        if (i):
            if (lenOf_match and (lenOf_match<=3)):
                _input = new_input
            else:
                break

    return _input


def main():
    opt = "help"
    while(opt):
        print('-' * 25)
        whatToDo(opt)
        opt = getOpt(False)


if __name__ == "__main__":
    main()
