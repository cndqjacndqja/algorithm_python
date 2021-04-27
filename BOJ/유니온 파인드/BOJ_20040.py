n, m = map(int, input().split())
data = [[] for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    data[i] = [a, b]

parent = [i for i in range(n)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

flag = 0
count = 1
for i in range(m):
    x, y = data[i]
    if find(parent, x) == find(parent, y):
        flag = 1
        break
    else:
        union(parent, x, y)
        count += 1

if flag == 0 and count == m+1:
    count = 0
print(count)
