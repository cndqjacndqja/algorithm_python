n = int(input())

data = []


def back_tracking(cnt):
    for i in range(1, cnt // 2 + 1):
        if data[-i:] == data[-i * 2:-i]:
            return -1

    if cnt == n:
        for i in range(n):
            print(data[i], end='')
        return 0
    for i in range(1, 4):
        data.append(i)
        if back_tracking(cnt + 1) == 0:
            return 0
        data.pop()


back_tracking(0)
