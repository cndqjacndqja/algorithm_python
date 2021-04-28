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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    data = []
    sum_data = 0
    for _ in range(n):
        a, b, cost = map(int, input().split())
        data.append((cost, a, b))
        sum_data += cost
    data.sort()
    result = 0
    for i in data:
        cost, x, y = i
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            result += cost
    print(sum_data-result)
