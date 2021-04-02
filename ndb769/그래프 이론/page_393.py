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


def solved():
    data = [[] for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]

    for i in range(1, n + 1):
        com = list(map(int, input().split()))
        for j in range(n):
            if com[j] == 1:
                data[i].append(j + 1)

    for i in range(1, n + 1):
        for j in data[i]:
            union(parent, i, j)

    result = list(map(int, input().split()))
    result_p = find(parent, result.pop())
    for i in result:
        if result_p != find(parent, i):
            print("NO")
            return
    print("YES")


solved()
