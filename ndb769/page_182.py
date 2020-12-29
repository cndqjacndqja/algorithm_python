n, k = map(int, input().split())

data1 = []
data2 = []

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort(reverse=True)

for i in range(k):
    data1[i], data2[i] = data2[i], data1[i]

print(sum(data1))