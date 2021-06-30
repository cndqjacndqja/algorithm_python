def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[a] = b


def solved(paths):
    dic = {}
    paths.sort()
    for i in paths:
        a, b = i
        dic[a] = a
        dic[b] = b

    for i in paths:
        a, b = i
        union(dic, a, b)
    print(dic)
    check = [False for _ in range(1000001)]
    result = []

    for i in paths:
        a, b = i
        parent = dic[a]
        if not check[parent]:
            check[parent] = True
            result.append(a)
            result.append(parent)
    print(result)


# solved([[1, 2], [4, 5], [10, 9], [3, 4]])
solved([[1, 2], [2, 3], [3, 4], [8, 7], [7, 6]])
# [[1, 2], [4, 5], [10, 9], [3, 4]]
