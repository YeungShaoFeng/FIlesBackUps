import os
import sys
import time
import getopt
from small_2 import Small


symbolNum = 0x17


def judge(password):
    password = confirm() if (not password) else password
    return password


def confirm():
    print(">aRe yOu suRe iT iS eMptY ?\n HIt \'enTer\' tO cOnFiRm:>\n oR inPuT tHe pasSwoRd. ")
    answer = input("> ")
    answer = '\u6797\u6eaa' if (not answer) else answer
    return answer


def pmt(mode):
    if(mode):
        print(">\'e\'       live encryption. ")
        print(">\'d\'       live decryption. ")
        print(">\'ef\'      file encryption. ")
        print(">\'df\'      file decryption. ")
        print(">hIt \'enter\' to quite. ")
        print(">\'-h\' or \'--help\' for help. ")
    opt = input("@yOu: ")
    return opt


def toSingle(mode):
    backstate = False
    string = input('>string: ')
    if (not string):
        print('-'*symbolNum)
        return backstate
    password = judge(input('>password: '))
    t1 = time.perf_counter()    
    obj = Small(string, password)
    obj.smallin(0x1) if(mode == 'e') else obj.smallout(0x1, 0x0)
    obj.tozero()
    t2 = time.perf_counter()    
    return t2-t1


def toFile(mode):
    backstate = False
    inputFile = input('>input file route: ')
    if (not inputFile):
        return backstate
    while(not os.path.isfile(inputFile)):
        print('Oops, invalid path!!!')
        inputFile = input('>input file route\n (hit enter to go back): ')
        if (not inputFile):
            return backstate
    password = judge(input('>password: '))
    backstate = withFile(mode, inputFile, password)
    return backstate


def withFile(mode, inputFile, password):
    backstate = False
    No = 0x1
    t1 = time.perf_counter()
    try:
        if (mode == 'ef'):
            with open(inputFile, 'r') as fi:
                outputFile = inputFile+'.bin'
                with open(outputFile, 'wb') as fo:
                    fo.write(b'\u6797\u6eaa\r\n')
                    line = fi.readline()
                    while(line):
                        if (line != '\r\n' and line != '\n'):
                            obj = Small(line.strip(), password)
                            obj.smallin(0x0)
                            fo.write(bytes(obj.string, encoding='utf-8'))
                            obj.tozero()
                        else:
                            No = No
                        No += 1
                        line = fi.readline()
                        if (not line):
                            break
                        fo.write(b'\r\n')
                    print(f'Totaly {No} lines. ')

        elif(mode == 'df'):
            with open(inputFile, 'rb') as fi:
                outputFile = inputFile.strip('.bin')
                with open(outputFile, 'w', encoding='UTF-8') as fo:
                    line = fi.readline().decode('utf-8')
                    if (line != '\\u6797\\u6eaa\r\n'):  # [:0xe]
                        print('NOT LINXI FILE!')
                        return backstate
                    line = fi.readline().decode('utf-8')
                    while(line):
                        if (line != '\r\n' and line != '\n'):
                            obj = Small(line.strip(), password)
                            obj.smallout(0x0, 0x1)
                            fo.write(obj.string)
                            obj.tozero()
                        else:
                            No = No
                        line = fi.readline().decode('utf-8')
                        if (not line):
                            break
                        fo.write('\n')
                        No += 1
                    print(f'Totaly {No} lines. ')
    except(TypeError):
        print("WRONG PASSWORD(　o=^•ェ•)o　┏━┓")
        raise
    t2 = time.perf_counter()        
    return t2-t1


def toExit():
    print(">bYe86")
    sys.exit(0x0)


# def toTerminal(argv):
#     useage = 'main.py -d <dir> -f <file> -m <mode> -p <password>'
#     try:
#         opts, args = getopt.getopt(argv, "hd:f:m:p", ["help", "dir=", "file=", "mode=", "password="])
#     except getopt.GetoptError:#getopt.GetoptError
#         raise
#         print(useage)
#         exit(2)
#     for opt, arg in opts:
#         if opt in ("-h", "--help"):
#             print(useage)
#             sys.exit()
#         elif opt in ("-f", "--file"):
#             inputFile = arg
#             if (opt in ("-m", "--mode")):
#                 mode = arg
#                 if (opt in ("-p", "--password")):
#                     withFile(mode, inputFile, arg)


def whatToDo(opt):
    if(opt == 'e'):
        TIME = toSingle(opt)
    elif(opt == 'd'):
        TIME = toSingle(opt)
    elif(opt == 'ef'):
        TIME = toFile(opt)
    elif(opt == 'df'):
        TIME = toFile(opt)
    elif(opt in ('-h', '--help')):
        TIME = whatToDo(pmt(0x1))
    elif(opt == ''):
        toExit()
    elif(('-f' in opt and '-p' in opt) or ('-d' in opt and '-p' in opt)):
        TIME = toTerminal(opt)
    else:
        print('>sorry, Not supported. ;<')
    print(f'Time: {TIME}s. ') if (TIME) else 1+1
    return True


def main(argv):
    print('-'*symbolNum)
    junk = whatToDo(argv) if (argv) else whatToDo(pmt(0x1))
    while(True):
        print('-'*symbolNum)
        whatToDo(pmt(0x0))


if __name__ == "__main__":
    main(sys.argv[1:])
