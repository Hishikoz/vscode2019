from multiprocessing import Process
from threading import Thread
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d]。' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def download_thread(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))

def test1():
    start = time()
    p1 = Process(target=download_task, args=('文件1',))
    p1.start()
    p2 = Process(target=download_task, args=('文件2',))
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print('总共耗费了%.2f秒。' % (end - start))


def test2():
    start = time()
    t1 = Thread(target=download_thread('文件1'))
    t1.start()
    t2 = Thread(target=download_thread('文件2'))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒。' % (end - start))


def test3():
    start = time()
    t1 = DownloadTask('文件1')
    t1.start()
    t2 = DownloadTask('文件2')
    t2.start()
    t1.join()
    t2.join()

    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


def main():
    test3()


if __name__ == '__main__':
    main()
