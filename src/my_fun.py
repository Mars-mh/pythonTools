import numpy as np
import scipy.stats
import math


# 距离函数
def get_distance(x, y):
    print("processing NO.{}".format(y.index[0]))

    delta_time = abs(x['time_new'].iloc[0] - y['time_new'].iloc[0])

    p = np.array(x[['sym', 'sen', 'con']])[0]
    q = np.array(y[['sym', 'sen', 'con']])[0]

    m = (p + q) / 2

    p = [float(i) for i in p]
    q = [float(i) for i in q]
    m = [float(i) for i in m]

    r = 0.5 * scipy.stats.entropy(p, m, base=2) + 0.5 * scipy.stats.entropy(q, m, base=2)

    time_cost = (1./math.pow(delta_time+2, 1.8))
    r = r / time_cost

    return r
