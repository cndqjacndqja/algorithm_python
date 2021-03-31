n, m = map(int, input().split())

data = [i for i in range(n + 1)]


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
    for _ in range(m):
        com, a, b = map(int, input().split())

        if com == 0:
            union(data, a, b)
        elif com == 1:
            if find(data, a) == find(data, b):
                print("YES")
            else:
                print("NO")


solved()
