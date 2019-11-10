import time
import hashlib


class shiftIt:
    def __init__(self, password, plainText):
        self.password = ord
        self.plainText = plainText
        self.cipherText = ''


    def shift(self):
        
        plainText = list(self.plainText)
        for i in range(len(plainText)):
            plainText[i] = chr(ord(plainText[i])*2 % 255)
        print(plainText)
        self.plainText = ''.join(plainText)
        return self.plainText


    def unshift(self):
        cipherText = list(self.plainText)
        for i in range(len(cipherText)):
            if(ord(cipherText[i])%2==0):
                cipherText[i] = chr(ord(cipherText[i])//2)
            else:
                cipherText[i] = chr((ord(cipherText[i])+255)//2)
        print(cipherText)
        self.cipherText = ''.join(cipherText)
        return self.cipherText

    def hasher(self, text):
        hash_object = hashlib.sha256(text.encode('utf-8'))
        hex_digt = hash_object.hexdigest()
        print(f"hash_text: {hex_digt}")
        return hex_digt

plainText = input("plainText: ")
password = input("password: ")
shiftIt_obj = shiftIt(plainText, password)
shiftIt_obj.shift()

print(shiftIt_obj.shift())
print(shiftIt_obj.unshift())



# yuanli

#print(f"i\ti*2\ti*2%255")
#for i in range(256):
#    print(f"{i}\t{i*2}\t{i*2%255}")
