RANGE_DATA = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
LEN_RAN = len(RANGE_DATA)
MAX_SUM = 0


def find_max_range_1(x: list):
    max_sum = 0
    max_l = 0
    max_r = 0
    for l in range(LEN_RAN):
        for r in range(l, LEN_RAN):
            tem = sum(x[l: r+1])
            if tem >= max_sum:
                max_sum = tem
                max_l = l
                max_r = r

    print("最值为：{}，其区间为：{}-{}".format(max_sum, max_l, max_r))


def find_max_range_2(x: list):
    max_sum = 0
    max_l = 0
    max_r = 0

    for l in range(LEN_RAN):
        tem = 0
        for r in range(l, LEN_RAN):
            tem += x[r]
            if tem > max_sum:
                max_sum = tem
                max_r = r
                max_l = l

    print("最值为：{}，其区间为：{}-{}".format(max_sum, max_l, max_r))


def find_max_range_3(x: list):

    def helper(values: list, left: int, right: int):
        # 出口
        if left == right:
            return [values[left], left, right]

        # 递归
        k = int((left + right)/2)

        res_l = helper(values, left, k)
        res_r = helper(values, k + 1, right)

        # 结果合并
        if res_l[2] + 1 == res_r[1]:

            if res_l[0] > 0 and res_r[0] > 0:
                return [res_r[0] + res_l[0], res_l[1], res_r[2]]

            elif res_l[0] > res_r[0]:
                return res_l
            else:
                return res_r
        else:

            tem = sum(values[res_l[1]: res_r[2] + 1])
            tem_res = [tem, res_l[1], res_r[2]]

            if res_l[0] > res_r[0]:
                if tem > res_l[0]:
                    return tem_res
                else:
                    return res_l
            else:
                if tem > res_r[0]:
                    return tem_res
                else:
                    return res_r

    res = helper(x, 0, LEN_RAN-1)
    print("最值为：{}，其区间为：{}-{}".format(res[0], res[1], res[2]))


def find_max_range_4(x: list):

    return 0


find_max_range_1(RANGE_DATA)
find_max_range_2(RANGE_DATA)
find_max_range_3(RANGE_DATA)




