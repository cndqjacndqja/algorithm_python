import sys
from bisect import bisect_left


# 시간을 숫자로 변환
def time_trans(time):
    time_m = int(time[:2])
    time_s = int(time[3:5])
    time_m = time_m * 60

    return time_m + time_s


def trans_total_time(time):
    time_h = int(time[:2])
    time_m = int(time[3:5])
    time_s = int(time[6:8])

    time_h = time_h * 60 * 60
    time_m = time_m * 60
    return time_h + time_m + time_s


def solved():
    n, total_time = input().split()
    n = int(n)
    total_time = trans_total_time(total_time)

    data = []
    for _ in range(n):
        data.append(time_trans(input()))
    result = bisect_find(data, total_time)
    print(result[0], result[1])


def bisect_find(data, total):
    count = 0
    result = []
    for i in range(len(data)):
        sum = 0
        for j in range(i, len(data)):
            sum += data[j]
            count += 1
            if sum >= total:
                result.append([count, i+1])
                count = 0
                break
    result.sort(key= lambda x:(x[0], -x[1]))
    return [result[-1][0], result[-1][1]]


solved()
