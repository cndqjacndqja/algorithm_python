result_data = 0

def cal(data, high):
    result = 0
    for i in data:
        if i - high > 0:
            result += (i - high)
    return result


def binary_search(start, end, data, m):
    global result_data
    if start > end:
        return
    mid = (start + end) // 2
    result = cal(data, mid)

    if result >= m:
        result_data = mid
        binary_search(mid+1, end, data, m)
    else:
        binary_search(start, mid - 1, data, m)





def solved():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    binary_search(1, max(data), data, m)
    print(result_data)

solved()



