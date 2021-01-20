import copy
n = int(input())

data1 = list(map(int, input().split()))
data2 = copy.deepcopy(data1)

for i in range(n):
    for j in range(i, n):
        if data2[i] < data2[j]:
            data1[j] = max(data1[j], data2[j] + data1[i])

print(max(data1))
