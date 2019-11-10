# import os
# import sys
# import time
import hashlib


class Small:
    def __init__(self, plainstring, password):
        self.uni = 0x100009
        self.password = password
        self.string = plainstring
        return None

    # 更新数据
    def update(self):
        if (self.password):
            self.password_hash_string = Small.hasher(self, self.password)
            self.password_hash_value_sum = Small.sum(self, list(self.password_hash_string))
        else:
            self.password_hash_value_sum = 0x0
        return None

    # 清空数据
    def tozero(self):
        self.uni = b'\u6797\u6eaa'
        self.password = b'\u6797\u6eaa'
        self.string = b'\u6797\u6eaa'
        self.plainstring_hash_value = b'\u6797\u6eaa'
        self.password_hash_string = b'\u6797\u6eaa'
        self.password_hash_value_sum = b'\u6797\u6eaa'
        return None

    # 加密
    def smallin(self, printMode):
        Small.update(self)
        self.string = Small.shift(self, self.string, self.password_hash_string) # , self.password_hash_value_sum, self.uni
        Gone = Small.stringPrint(self, 'cipher', self.string) if (printMode) else 1
        return None

    # 解密
    def smallout(self, printMode, fileMode):
        Small.update(self)
        self.string = Small.unshift(self, self.string, self.password_hash_string, fileMode) # , self.password_hash_value_sum, self.uni
        Small.stringPrint(self, 'origin', self.string) if (printMode) else 1+1 
        return None

    # 输出密文


    def stringPrint(self, mode, string):
        if(mode == 'cipher'):
            l = len(string)+0xf
            print('*' * l)
            print(f'>cipher string: {string}')
            print('*' * l)
        else:
            l = len(string)+0x14
            print('*' * l)
            print(f'>original content: {string}')
            print('*' * l)
        return True

    # 哈希值计算


    def hasher(self, string):
        hash_object = hashlib.sha512(string.encode('utf-8'))
        hex_digt = hash_object.hexdigest()
        return hex_digt

    # 哈希值求和


    def sum(self, lista):
        sumup = 0x0
        for i in range(len(lista)):
            sumup += ord(lista[i])
        return sumup + 0x224

    # 正移加密


    def shift(self, string, shiftString): # , shiftNum, modeNum
        string, shiftString = list(string), list(shiftString)
        length = len(string) if (len(string) < len(shiftString)) else len(shiftString)
        for i in range(length):
            string[i] = chr(ord(string[i]) + ord(shiftString[i])) #  + shiftNum) % modeNum)
        return ''.join(string)

    # 反移解密


    def unshift(self, string, shiftString, fileMode): # , shiftNum, modeNum
        string, shiftString = list(string), list(shiftString)
        length = len(shiftString) if (len(string) > len(shiftString)) else len(string)
        try:
            if (fileMode):
                if (isinstance(string[0], str)):
                    for i in range(length):
                        if(ord(string[i]) > shiftNum):
                            string[i] = chr(ord(string[i]) - ord(shiftString[i])) #  - shiftNum
                        else:
                            string[i] = chr(ord(string[i]) - ord(shiftString[i])) #  + modeNum  - shiftNum
                    string = ''.join(string)
                else:
                    print("Another showed up!!!")
            else:
                if (isinstance(string[0], str)):
                    for i in range(length):
                        if(ord(string[i]) > shiftNum):
                            string[i] = chr(ord(string[i]) - ord(shiftString[i]))#  - shiftNum)
                        else:
                            string[i] = chr(ord(string[i]) - ord(shiftString[i])) # + modeNum   - shiftNum
                    string = ''.join(string)
                else:
                    print("Another showed up!!!")
        except(ValueError):
            raise
        return string


