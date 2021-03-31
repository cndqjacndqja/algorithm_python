n, m = map(int, input().split())


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


def kruskal():
    data = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        data.append((c, a, b))

    data.sort()
    parent = [i for i in range(n+1)]
    result = []
    for i in data:
        cost, a, b = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result.append(cost)
    result.sort()
    print(sum(result) - result[-1])

kruskal()

