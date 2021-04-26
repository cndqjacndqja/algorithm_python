import sys
input = sys.stdin.readline


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


def solved():
    for _ in range(m):
        com, x, y = map(int, input().split())
        if com == 0:
            union(parent, x, y)
        elif com == 1:
            if find_parent(parent, x) == find_parent(parent, y):
                print("YES")
            else:
                print("NO")

solved()
