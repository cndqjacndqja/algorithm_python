from itertools import combinations
import time

start_time = time.time()

n = int(input())
data = list(map(int, input().split()))

result = []


def combi():
    for i in range(1, len(data) + 1):
        combi_data = combinations(data, i)

        for c in combi_data:
            plus_data = sum(c)
            if plus_data not in result:
                result.append(plus_data)
    result.sort()


def solved():
    for i in range(1, sum(data)+2):
        if i not in result:
            print(i)
            return


combi()
solved()
end_time = time.time()

print(end_time-start_time)