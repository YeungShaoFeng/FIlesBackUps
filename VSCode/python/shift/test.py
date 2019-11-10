# import os
# import hashlib


# def hasher(text):
#     hash_object = hashlib.sha512(text.encode('utf-8'))
#     hex_digt = hash_object.hexdigest()
#     # print(f"hash_text: {hex_digt}")
#     return hex_digt

# a = 'asdfghjkkl;'
# hash_value = hasher(a)
# print(hash_value)
# a = list(a)
# hash_value = list(hash_value)
# if (len(hash_value) > len(a)):
#     length = len(a)
# else:
#     length = len(hash_value)

# for i in range(length):
#     a[i] = chr(ord(a[i]) + ord(hash_value[i]))
# print(a)
# length = len(a) if (len(a)>len(hash_value)) else len(hash_value)
# print(length)
# linxi = '\u6797\u6eaa'
# uni = 0x100009
# my = 0x1a24
# b = []
# text = '0x100009'
# a = hasher(text)
# c = []
# lines = []
# path = (os.getcwd() + '\\encrypout.bin') if (True) else 'False'
# with open(path, 'rb') as fi:
#     for line in fi:
#         print(line)

# print(lines[0][:14])
# if (lines[0][:14]=='\\u6797\\u6eaa\r\n'):
#     print('\\u6797\\u6eaa')
# for i in range(len(lines)):
#     print(len(lines[i]), end='\t')
#     print(lines[i])
# def judge(password):
#     password = confirm() if (not password) else password
#     return password

# def confirm():
#     print(">aRe yOu suRe iT iS eMptY ?\n HIt \'enTer\' tO cOnFiRm:>\n oR inPuT tHe pasSwoRd. ")
#     answer = input("> ")
#     answer = '\u6797\u6eaa' if (not answer) else answer
#     return answer


# # print(judge(input('> ')))

# def a(string):
#     print(string)
# # string = 'string'
# # a(string) if (input('> ')) else print('False')





import os

Files = []
def withDir(DIR='.'):
    for root, dirs, files in os.walk(DIR, topdown=False):
        a, b = list(root), list('\\data')
        b.reverse()
        for var in b:
            a.insert(1, var)
        root = ''.join(a)
        os.makedirs(root) if (not os.path.exists(root)) else print('root already exists. ')
        for name in files:
            FILE_ = os.path.join(root, name)
            with open(FILE_, 'wb') as f:
                f.write(bytes('hello. \n', encoding='utf-8'))
                f.close()
            Files.append(FILE_)
        # for name in dirs:
        #     DIR_ = os.path.join(root, name)
        #     # print(DIR_)
        #     Dirs.append(DIR_)

# walkIn()
print('Tinnnn~')
def haha(a, b=None):
    print(f'{a}, {b}')
haha(1, b=3)
# print(Files)
# print()
# print(Dirs)


# import os
# import sys
# def mai(argv):
#     if (argv):
#         useage = 'main.py -d <dir> -f <file> -m <mode> -p <password>'
#         try:
#             opts, args = sys.getopt(argv,"hd:f:m:p", ["help", "dir=","file=", "mode=", "password="])
#         except: # GetoptError
#             print(useage)
#             exit(2)
#         print(opts)
#         for opt, arg in opts:
#             if opt in ("-h", "--help"):
#                 print(useage)
#                 sys.exit()
#             elif opt in ("-d", "--dir"):
#                 pass
                # withFile()

    # print('-'*symbolNum)
    # whatToDo(pmt(0x1))
    # print('-'*symbolNum)    
    # while(True):
    #     whatToDo(pmt(0x0))
    #     print('-'*symbolNum)

# if __name__ == "__main__":
#     main(sys.argv[1:])

# opt = ['-f', 'file', '-p', 'password']
# if(('-f' in opt and '-p' in opt) or ('-d' in opt and '-p' in opt)):
#     print(True)

# opt = ['-f', 'file', 'password']
# if(('-f' in opt and '-p' in opt) or ('-d' in opt and '-p' in opt)):
#     print(True)
# import time as t
# for i in range(24000, 30000):
#     print(f"{i}:{chr(i)}", end='\t')
#     print('\n') if (i != 0 and i % 16 == 0) else 1+1
#     # t.sleep(0.01)
# '''
# normal: 10000
#     漢字: 11904
# unormal:  口 6688
         

# '''