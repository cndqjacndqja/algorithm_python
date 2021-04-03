n = int(input())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solved():
    x, y, z = [], [], []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append((a, i))
        y.append((b, i))
        z.append((c, i))

    x.sort()
    y.sort()
    z.sort()

    data = []
    for i in range(n - 1):
        data.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
        data.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
        data.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

    data.sort()
    parent = [i for i in range(n)]
    result = 0
    for i in data:
        cost, a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    print(result)

solved()
