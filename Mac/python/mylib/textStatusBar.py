#! usr/bin/env
# -*- coding : utf-8 -*-

from os import popen as os_popen


class TextStatusBar:
    def __init__(self, scale):
        self.scale = scale
        self.length = TextStatusBar.getColumns(self) // 2 - 7
        self.cnt = 0
        self.indentation = ""

    def show(self, onlyPercets=False, indentation="", willReturn=False, refresh=False):
        self.indentation = indentation
        if not refresh:
            self.cnt += 1
        percents = self.cnt / self.scale
        # 动态跟新显示宽度
        self.length = TextStatusBar.getColumns(self) // 2 - 7
        pound = int(percents * self.length)
        space = int(self.length - pound)
        a = "#" * pound
        b = " " * space
        c = (self.cnt / self.scale) * 100
        if indentation != "":
            if onlyPercets:
                fmt = "{:^3.0f}%".format(c)
            else:
                fmt = "\r{}[{}{}] {:^3.0f}%".format(indentation, a, b, c)
        else:
            fmt = "\r[{}{}] {:^3.0f}%".format(a, b, c)

        return fmt if willReturn else print(fmt, end="")

    def hide(self):
        self.cnt += 1

    def clear(self):
        self.cnt = 0

    def getColumns(self):
        return int(os_popen("stty size", "r").read().split()[1])

    def refresh(self):
        return TextStatusBar.show(
            self, indentation=self.indentation, willReturn=True, refresh=True
        )


def main():
    from time import sleep as t_sleep

    # Single bar
    for j in range(20):
        bar = TextStatusBar(j)
        for i in range(j):
            t_sleep(0.1)
            bar.show(indentation="|  |")
        print()

    # Double bars
    a, b = 10, 20
    bar1 = TextStatusBar(a)
    bar2 = TextStatusBar(b)

    for i in range(a):
        bar1.hide()
        for j in range(b):
            t_sleep(0.5)
            bar2.show(indentation=bar1.refresh())
        bar2.clear()


if __name__ == "__main__":
    main()
