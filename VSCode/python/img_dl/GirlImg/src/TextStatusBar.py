#! usr/bin/env
# -*- coding : utf-8 -*-
import time


class TextStatusBar:
    def __init__(self, scale):
        self.scale = scale
        self.length = 50
        self.cnt = 0

    def show(self, indentation=''):
        self.cnt += 1
        percents = self.cnt / self.scale
        stars = int(percents * self.length)
        dots = int(self.length - stars)
        # print('C: {}\tP: {}\tS: {}\tD: {}'.format(self.cnt, percents, stars, dots))
        a = "*" * stars
        b = "." * dots
        c = (self.cnt / self.scale) * 100
        if (indentation != ''):
            print("\r{}{:^3.0f}%[{}->{}]".format(indentation, c,a,b),end = "")
        else:
            print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end = "")

def main():
    for j in range(20):
        bar = TextStatusBar(j)
        for i in range(j):
            time.sleep(0.5)
            bar.show("|  |")
        # print()

if (__name__ == "__main__"):
    main()