import math
import matplotlib.pyplot as plt  


n = 1000
a, x_2, y_3, sub = [None] * n, [None] * n, [None] * n, [None] * n
for i in range(n):
    a[i] = math.log(2**i, 3)

for i in range(n):
    x_2[i] = 2**i
    y_3[i] = 3**a[i]
    sub[i] = x_2[i] - y_3[i]

for i in range(n):
    print(f'i: {i}\na[i]: {a[i]}\n2^x: {2**i}\n3^y: {3**a[i]}\n2^x-3^y: {2**i-3**a[i]}')
    print('-'*100)
    # if (3**a[i]==2**i):
    #     print(True)
    # else:
    #     print(False)
plt.plot(a)
plt.show()
# plt.plot(x_2)
# plt.show()
# plt.plot(y_3)
# plt.show()
# plt.plot(sub)
# plt.show()