def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b, count):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
        count[a] += count[b]
    elif a > b:
        parent[a] = b
        count[b] += count[a]




def solved():
    for _ in range(int(input())):
        n = int(input())
        parent = {}
        count = {}
        for _ in range(n):
            a, b = input().split()
            if a not in parent:
                parent[a] = a
                count[a] = 1
            if b not in parent:
                parent[b] = b
                count[b] = 1
            union(parent, a, b, count)

            if a < b:
                print(count[find(parent, a)])
            else:
                print(count[find(parent, b)])


solved()
