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
    g = int(input())
    p = int(input())
    parent = [i for i in range(p+1)]
    count = 0
    for _ in range(p):
        n = int(input())
        root = find(parent, n)
        if root == 0:
            break
        else:
            union(parent, root-1, root)
            count += 1
    print(count)

solved()
