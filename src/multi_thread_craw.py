import common
import threading
import time


# 单线程
def single_thread():
    print('single_thread begin...')
    for url in common.urls:
        common.craw(url)
    print('single_thread end...')


# 多线程
def multi_thread():
    print('multi_thread begin...')
    threads = []
    for url in common.urls:
        threads.append(
            threading.Thread(target=common.craw, args=(url, ))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('multi_thread end...')


if __name__ == '__main__':
    time_s = time.time()
    single_thread()
    time_e = time.time()
    print('single_thread cost {} seconds'.format(time_e - time_s))

    time_s = time.time()
    multi_thread()
    time_e = time.time()
    print('multi_thread cost {} seconds'.format(time_e - time_s))
