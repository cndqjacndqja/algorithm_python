def solution(lottos, win_nums):
    count = 0
    zero_count = 0
    for i in win_nums:
        if i in lottos:
            count += 1

    for i in lottos:
        if i == 0:
            zero_count += 1

    return [find_rate(zero_count + count), find_rate(count)]


def find_rate(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
