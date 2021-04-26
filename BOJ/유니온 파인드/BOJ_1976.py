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
    elif b < a:
        parent[a] = b


def solved():
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            if data[j] == 1:
                union(parent, i+1, j+1)

    plan = list(map(int, input().split()))
    flag = "YES"
    parent_node = parent[plan[0]]
    for i in plan:
        if find(parent, parent_node) != find(parent, i):
            flag = "NO"
    print(flag)

solved()
