n, m = map(int, input().split())
data = []
total_cost = 0
for _ in range(m):
    x, y, cost = map(int, input().split())
    total_cost += cost
    data.append((cost, x, y))


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
    data.sort()
    result = 0
    parent = [i for i in range(n)]

    for i in data:
        cost, x, y = i
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            result += cost

    print(total_cost - result)


kruskal()
