import threading
import multiprocessing
import pandas as pd
import my_fun
import queue
import time


def get_dis(x, data, q_):
    for my_index, item in data.iterrows():
        item = pd.DataFrame(item).T

        distance = my_fun.get_distance(x, item)

        q_.put(
            {my_index: distance}
        )


if __name__ == '__main__':

    path = '/Users/mahao/PycharmProjects/pythonTools/data/三维度数据归一化_0309.xlsx'
    excel = pd.read_excel(path, index_col=0)

    n = len(excel)
    range_n = [i for i in range(100, n, 900)]
    q = multiprocessing.Manager().Queue()

    for _, i in excel.iterrows():
        time_s = time.time()
        x_frame = pd.DataFrame(i).T
        process = []

        for j in range_n:
            if j == range_n[-1]:
                data_frame = excel[j - 100: n]
            else:
                data_frame = excel[j-100:j]

            process.append(
                multiprocessing.Process(target=get_dis, args=(x_frame, data_frame, q, ))
            )

        [i.start() for i in process]
        [i.join() for i in process]
        time_e = time.time()

        print('cost {} - {} = {}'.format(time_e, time_s, time_e - time_s))
        break



