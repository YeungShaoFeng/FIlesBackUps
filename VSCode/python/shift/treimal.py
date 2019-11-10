import sys
import time
import random
from myway_2 import Tre


show = '1'
notShow = '0'
# main funcs
# work with file
def workWithFile(inputfile, outputfile, aimtype):
    with open(inputfile, 'r') as fi:
        with open(outputfile, 'w') as fo:
            line = fi.readline().strip() 
            while(line):
                if (line):
                    num = Tre(line, aimtype, notShow)
                    num.start()
                    cnt = -1
                    for var in num.cnt:
                        cnt += 1
                        for i in range(var):
                            fo.write(str(num.Tree[cnt][i]))
                        fo.write('\n')
                line = fi.readline().strip()


# work with num
def workWithNum(num, aimtype):
    dec = Tre(inputFliter(num), inputFliter(aimtype), inputFliter(show))
    dec.start()


# random number writing
def randomWrite(fi):
    with open(fi, 'w') as f:
        for i in range(3):
            f.write(str(random.randint(1000000, 1000000000)))
            f.write('\n')


# input fliter
def inputFliter(data):
    data = data.replace(' ', '').replace("\u202c", '').split(',')
    for var in data:
        if(var==''):
            data.remove(var)
    return data


# options prompt for users
def optPmt():
    print('-'*29)
    print("\'r\'    random writing to file")
    print("\'f\'    work with file")
    print("\'n\'    work with num(s)")
    print("\'q\'    quit")
    print('-'*29)
    opt = input("@you#~ ")
    # while(not opt):
    #     empty()
    #     opt = input("@you#~ ")
    return opt


# options implementations
# random numbers
def goR():
    fi = input("File route: ")
    while(not fi):
        whatToDo(optPmt())
    randomWrite(fi)
# work with nums
def goN():
    num = input("Num(s)(\',\' saprated): ")
    while (not num):
        num = optPmt()
        whatToDo(num)
    aimtype = input("aimtype(s)(\',\' saprated): ")
    if(not aimtype):
        aimtype = '2, 3, 8, 16'
    workWithNum(num, aimtype)
# work with file
def goF():
    fi = input("Input file: ")
    if (not fi):
        whatToDo(optPmt())
    fo = input("outputfile: ")
    aimtype = input("aimtype(s)(\',\' saprated): ")
    workWithFile(fi, fo, aimtype)
# to quit
def goQ():
    print('bYe')
    sys.exit(0)


# empty type-in 
def empty():
        print("#"*39)
        print("#OoOwaht! You didn't type in anything!#")
        print("#Maybe let's do this one more time.   #")
        print("#"*39)


# user options handling
def whatToDo(opt):
    if (opt=='r'):
        goR()
    elif(opt=='n'):
        goN()
    elif(opt=='f'):
        goF()
    elif(opt=='q'):
        goQ()
    opt = optPmt()
    while(not opt):
        empty()
        opt = optPmt()
    whatToDo(opt)


def main():
    opt = optPmt()
    while(not opt):
        empty()
        opt = optPmt()
    while(opt != 'q'):
        whatToDo(opt)
    goQ()


main()


def main(argv):
    #start time benchmark
    t1 = time.perf_counter()
    #get options from the user and deal with them
    aimtype = ''
    num = ''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = sys.getopt(argv,"hn:i:o:a:",["num=","ifile=","ofile=", "atype="])
    except GetoptError:
        print('treimal.py -n <number> -i <inputfile> -o <outputfile>, -a <aimtype>')
        exit(2)
    for opt, arg in opts:
        if (opt == '-h'):
            print('treimal.py -n <number> -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--number"):
            num = arg
        elif opt in ("-a", "--aimtype"):
            aimtype = arg
        elif opt not in ("-a", "--aimtype"):
            aimtype = [2, 3, 8]     #[2, 3, 8, 16]
    # start converting
    if (inputfile):
        workWithFile(inputfile, outputfile, aimtype)
    elif (num):
        workWithNum(num, aimtype)
    #endtimebenchmark
    t2 = time.perf_counter()
    print(f' GO time is: {t2-t1} s. ')

if __name__ == "__main__":
   main(argv[1:])
