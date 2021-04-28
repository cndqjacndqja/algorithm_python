n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]


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


data = []
for _ in range(m):
    a, b, c = map(int, input().split())
    data.append((c, a, b))

data.sort()


def solved():
    result = 0
    for i in data:
        cost, x, y = i
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            result += cost

    print(result)

solved()
