from itertools import permutations
def solved():
    n = int(input())
    data = list(map(int, input().split()))

    data_per = list(permutations(data, len(data)))
    result = 0
    for i in data_per:
        result = max(result, cal(i))
    print(result)

def cal(data):
    sum = 0
    for i in range(len(data) - 1):
        sum += abs(data[i] - data[i+1])
    return sum

solved()