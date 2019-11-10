import math
import matplotlib.pyplot as plt

def cal(a, layers, n):
    for i in range(n):
        layers[i] = i ** a/10
    return layers

def doSub(layers, tail, head, n, deepth):
    deepth += 1
    head = not head
    tail += 1
    if (head):
        for i in range(n-tail):
            layers[i] = round(layers[i+n+1] - layers[i+n], ndigits=50)
    else:
        for i in range(n, n*2-tail):
            layers[i] = round(layers[i-n+1] - layers[i-n], ndigits=50)
    if (not (layers[0]==layers[1] or layers[n]==layers[n+1])):
        doSub(layers, tail, head, n, deepth)
    else:
        if (layers[0]==layers[1]):
            layers[2*n-1] = layers[0]
        else:
            layers[2*n-1] = layers[n]
        layers[2*n] = deepth
        return

def main():
    a, deepth = 20, 0
    n, tail, head = 10, 0, True
    layers = [None] * (2 * n + 1)
    keys, deepths = [], []
    for i in range(2, a+1):
        doSub(cal(i, layers, n), tail, head, n, deepth)
        keys.append(layers[2*n-1])
        deepths.append(layers[2*n])
        print(f"a: {i}\tdeepth: {layers[2*n]}\tkey: {layers[2*n-1]}. ")
    # plt.plot(keys)
    # plt.plot(deepths)
    # plt.show()


main()