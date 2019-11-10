from sys import getsizeof
from time import perf_counter

class Tre:
    def __init__(self, num, aimtype, show):
        self.bus = 0
        self.num = num
        self.show = show
        self.aimtype = aimtype
        self.treNum, self.cnt = [0], [0]
        self.tree, self.Tree = [[0]], [[0]]

    def GO(self):
        def tre(self, i):
            def step(self, i):
                while(self.bus):
                    self.tree[i][self.cnt[i]] = self.bus % int(self.aimtype[i])
                    self.bus //= int(self.aimtype[i])
                    if (self.bus):
                        self.tree[i].append(0)
                        self.Tree[i].append(0)
                    self.cnt[i] += 1
                for j in range(self.cnt[i]-1, -1, -1):
                    self.Tree[i][self.cnt[i]-j-1] = self.tree[i][j]
                    self.treNum[i] += self.tree[i][j] * int(self.aimtype[i]) ** j
            def mapper(self):
                cnt = -1
                for var in self.Tree[i]:
                    cnt += 1
                    if (var == 10):
                        self.Tree[i][cnt] = 'A'
                    elif (var == 11):
                        self.Tree[i][cnt] = 'B'
                    elif (var == 12):
                        self.Tree[i][cnt] = 'C'
                    elif (var == 13):
                        self.Tree[i][cnt] = 'D'
                    elif (var == 14):
                        self.Tree[i][cnt] = 'E'
                    elif (var == 15):
                        self.Tree[i][cnt] = 'F'

            step(self, i)
            if(i < len(self.aimtype)-1):
                self.cnt.append(0)
                self.treNum.append(0)
                self.tree.append([0])
                self.Tree.append([0])
                self.bus = int(self.num)
            if (self.aimtype[i]=='16'):
                mapper(self)

        def treOut(self, i):
            def fout(self, var):
                for j in range(self.cnt[i]):
                    if (j>1 and j%var==0):
                        print(" ", end='')
                    print(self.Tree[i][j], end='')
                print()
            def judge(self, var):
                if (var==2):
                    print("Bin: ", end='')
                    fout(self, 4)
                elif (var==3):
                    print("Tre: ", end='')
                    fout(self, 3)
                elif (var==8):
                    print("Oct: ", end='') 
                    fout(self, 3)
                elif (var==16):
                    print("Hex: ", end='') 
                    fout(self, 4)
                elif (var):
                    print("Wha: ", end='') 
                    fout(self, 3)
            judge(self, int(self.aimtype[i]))


        self.bus = int(self.num)
        for i in range(len(self.aimtype)):
            tre(self, i)
            if (self.show):
                treOut(self, i)


def inputFliter(data):
    return data.replace(' ', '').replace("\u202c", '').split(',')
    

a = '255'
num = Tre(a, [2], 1)
num.GO()


# a = '9223372036854775807‬3148789465169745616516987987915321654979'
# nums = input("itself: ")
# aimtype = input("aimtype: ")
# t1 = perf_counter()
# nums = inputFliter(nums)
# if (aimtype!=''):
#     aimtype = inputFliter(aimtype)
# else:
#     aimtype = ['2', '3', '8']

# for var in nums:
#     print('-'*32)
#     print("Dec: {}".format(var))
#     for yar in aimtype:
        # num = Tre(var, yar)
        # num.GO()
# t2 = perf_counter()
# print(f'GO time is: {t2-t1} s. ')
