from os import mkdir as os_mkdir
from os.path import exists as os_path_exists
from queue import Queue
from threading import Thread as threading_Thread
from time import sleep as t_sleep

DOWNLOADER_EXIT = False
SAVER_EXIT = False


def saver(path, content=True, txt=False):
    dir_path = ''.join(path.split('/')[:-1])

    os_mkdir(dir_path) if not os_path_exists(dir_path) else True
    if content:
        with open(path, 'wb') as f:
            f.write(content)
    elif(txt):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)


class ThreadDownloader(threading_Thread):
    threadCounter = 0

    def __init__(self, threadName, urlsQueue, dataQueue):
        ThreadDownloader.threadCounter += 1
        super(ThreadDownloader, self).__init__()
        self.urlsQueue = urlsQueue
        self.dataQueue = dataQueue
        self.name = threadName
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        }

    def download(self, url, img=True):
        try:
            r = requests_get(url, headers=self.headers)
            r.raise_for_status
            r.encoding = r.apparent_encoding
        except:
            raise
        saver()
        # return "Succeesfully downloaded."
        return [url, r.content if img else r.text]

    def run(self):
        print(self.name + " started.")
        while not self.urlsQueue.empty():
            try:
                print("requesting...")
                # --T
                t_sleep(0.5)
                # --T
                content = ThreadDownloader.download(
                    self, self.urlsQueue.get(False))
                print(self.name + " putting content into dataQueue")
                self.dataQueue.put(content)
            except:
                pass
        print(self.name + "ended.")


class Downloader:
    def __init__(self, urlsLista):
        self.urlsLista = urlsLista
        self.urlsQueue = Downloader.listaToQueue(self, self.urlsLista)
        self.dataQueue = Queue(len(self.urlsLista))
        self.name = "Downloader Leader"

    def listaToQueue(self, urlsLista):
        myQueue = Queue(len(urlsLista))
        for url in urlsLista:
            myQueue.put(url)
        return myQueue

    def queueToLista(self, myQueue):
        data = []
        for i in range(myQueue.qusize()):
            data.append(myQueue.get())
        return data

    def go(self, threadNum=1, willReturn=False):
        threadDownloaders = []

        for i in range(threadNum):
            thread = ThreadDownloader(
                "THDW#" + str(i), self.urlsQueue, self.dataQueue)
            thread.start()
            threadDownloaders.append(thread)

        while not self.urlsQueue.empty():
            pass
        # while self.urlsQueue.empty():
        #     for thread in threadDownloaders:
        #         thread.exit()
        global DOWNLOADER_EXIT
        DOWNLOADER_EXIT = True
        for thread in threadDownloaders:
            thread.join()

        for i in range(self.dataQueue.qsize()):
            print(self.dataQueue.get())

        if willReturn:
            pass
        else:
            pass


def main():
    # urls = [
    #     "https://66.media.tumblr.com/a5bb71f25bb50c91f9a8f89248621453/16d47760d4919065-74/s640x960/901715d307a9d022d56dd9412e1c83bd40b9ddbc.jpg",
    #     "https://66.media.tumblr.com/3575d7085adb591455e913ded74d0e81/950e19fe0b98ff92-8b/s1280x1920/dda910b041756c706ff200362db71182a2bd8a04.jpg",
    #     "https://66.media.tumblr.com/e84361ead53e0418a1d39a2d8ff5109a/950e19fe0b98ff92-72/s1280x1920/9c2b2b67ab22e9fa9329a57d347f0de021dabedc.jpg",
    #     "https://66.media.tumblr.com/ec93f52dbec3225ae77bed95742635d9/950e19fe0b98ff92-67/s1280x1920/f5d5d0d3242f756174eed0e73622f4bdbb348e1d.jpg",
    #     "https://66.media.tumblr.com/eb6bcdee23076e7fb8ecd37d4566312c/tumblr_pyt25lPOpU1vx6cf2o1_1280.jpg",
    #     "https://66.media.tumblr.com/14add99d1bca85cf7d52be9d7c743f4a/tumblr_oe7qp3RAyO1s0ns5lo1_1280.jpg",
    #     "https://66.media.tumblr.com/c31d51056ba84fb57aad87802c38ac24/tumblr_pzki1xgvBT1xw2f7fo1_1280.jpg",
    #     "https://66.media.tumblr.com/23dbe4ccf43c806ec547560aa27a68ca/tumblr_pzenrw2d261xw2f7fo1_1280.jpg",
    #     "https://pbs.twimg.com/media/EHfNCS7XYAMMh4q.jpg",
    #     "https://66.media.tumblr.com/30beaac3cbcf7335c169ed25203354f5/8e45a34ed3d780f0-dd/s1280x1920/576495b5e8506e38788fe17521db8a36fbc39767.jpg",
    #     "http://www.jinqiuhui.net/upload/image/20190730/1564474154349255.jpg",
    #     "http://www.jinqiuhui.net/upload/image/20190730/1564474154800708.jpg",
    #     "https://66.media.tumblr.com/9ad4347a47765ea0f9a41680fb675da2/d17b95d5f13eef61-bf/s640x960/603cf7441010dfe548e63f1ccf83cce62af24451.jpg",
    #     "https://pbs.twimg.com/media/D8CgDveU0AAdXFk.jpg",
    #     "https://pbs.twimg.com/media/EHPke-WVAAA6yvQ.jpg",
    #     "https://66.media.tumblr.com/0d82846fe7c929c6972d63bee317b48e/tumblr_pxb6r6cPsm1y9dhm6o1_1280.jpg",
    #     "https://66.media.tumblr.com/bfaab0955147f65d62cc4d793c37c3a6/tumblr_pz5mk80Xt31xw2f7fo1_1280.jpg",
    #     "https://66.media.tumblr.com/fa0308cd6a194b4118e11201813ce5fd/tumblr_pza8v04n5t1tg9f61o1_1280.jpg",
    #     "https://66.media.tumblr.com/190998210226a6695f2602a22429b863/tumblr_poi8abH4oZ1tm3ddao1_1280.jpg",
    #     "https://66.media.tumblr.com/f17be82b893a6b979077f8ee930fd904/tumblr_pzbalgfGqO1y9dhm6o1_1280.jpg",
    # ]
    urls = [x for x in range(20)]
    downloader = Downloader(urls)
    downloader.go(threadNum=3)


if __name__ == "__main__":
    main()
