from sys import getsizeof
from time import perf_counter

class Tre:
    def __init__(self, num, aimtype, show):
        self.num = num
        self.show = show
        self.aimtype = aimtype
        self.i, self.j = 0, 0
        self.bus, self.treNum, self.cnt = [], [[0]], [[0]]
        self.tree, self.Tree = [[[0]]], [[[0]]]

    def start(self):
        def tre(self, inber):
            def step(self, inber, jack):
                while(self.bus[inber]):
                    self.tree[jack][inber][self.cnt[jack][inber]] = self.bus[inber] % self.aimtype[inber]
                    self.bus[inber] //= self.aimtype[inber]
                    if (self.bus[inber]):
                        self.tree[jack][inber].append(0)
                        self.Tree[jack][inber].append(0)
                    self.cnt[jack][inber] += 1
                for j in range(self.cnt[jack][inber]-1, -1, -1):
                    self.Tree[jack][inber][self.cnt[jack][inber]-j-1] = self.tree[jack][inber][j]
                    self.treNum[jack][inber] += self.tree[jack][inber][j] * self.aimtype[inber] ** j
            def toHex(self):
                cnt = -1
                for var in self.Tree[jack][inber]:
                    cnt += 1
                    if (var == 10):
                        self.Tree[jack][inber][cnt] = 'A'
                    elif (var == 11):
                        self.Tree[jack][inber][cnt] = 'B'
                    elif (var == 12):
                        self.Tree[jack][inber][cnt] = 'C'
                    elif (var == 13):
                        self.Tree[jack][inber][cnt] = 'D'
                    elif (var == 14):
                        self.Tree[jack][inber][cnt] = 'E'
                    elif (var == 15):
                        self.Tree[jack][inber][cnt] = 'F'

            step(self, inber, jack)
            if(inber < len(self.aimtype)-1):
                self.cnt[jack].append(0)
                self.treNum[jack].append(0)
                self.tree[jack].append([0])
                self.Tree[jack].append([0])
                # self.bus[i] = self.num[i]
            if (self.aimtype[inber]==16):
                toHex(self)

        def treOut(self, inber, jack):
            def fout(self, var):
                for j in range(self.cnt[jack][inber]):
                    if (j>1 and j%var==0):
                        print(" ", end='')
                    print(self.Tree[jack][inber][j], end='')
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
            judge(self, self.aimtype[inber])

        
        def inputToArray(self):
            def listToArray(lista):
                for i in range(len(lista)):
                    lista[i] = int(lista[i])
                return lista
            self.num = listToArray(self.num)
            self.aimtype = listToArray(self.aimtype)
            self.show = listToArray(self.show)
            for dd in range(len(self.num)):
                self.bus.append(self.num[dd])

        inputToArray(self)
        for jack in range(len(self.num)):
            for inber in range(len(self.aimtype)):
                tre(self, inber)
                if (self.show[0]):
                    print("-"*32)
                    print(f"Dec: {self.num[inber]}")
                    treOut(self, inber, jack)
                # for dd in range(len(self.num)):
                #     self.bus[dd] = self.num[dd]


def inputFliter(data):
    return data.replace(' ', '').replace("\u202c", '').split(',')
    
num = '255, 10'
aimtype = '2, 3'
show = '1'

ex = Tre(inputFliter(num), inputFliter(aimtype), inputFliter(show))
ex.start()
