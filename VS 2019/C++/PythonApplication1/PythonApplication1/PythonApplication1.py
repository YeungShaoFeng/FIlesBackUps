import numpy as np


a = np.arange(1, 40, 2, dtype='int64')
a = a.reshape(4,5)
b = np.arange(40, 1, -2, dtype='int64')
b = b.reshape(4,5)
c = a * b

print(a)
print(b)
print(c)



'''
name = input("Input your name: ")
fmt = "吃了没，{0}？"
print(fmt.format(name))
'''