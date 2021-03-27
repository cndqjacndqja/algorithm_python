INF = int(1e9)
def solved():
    n = int(input())
    data = {}

    for _ in range(n):
        a, b, c = input().split()
        c = int(c)
        if a not in data:
            data[a] = {}
        if b not in data:
            data[b] = {}

        data[a][b] = c
        data[b][a] = c
    result = []
    visited = []
    for a in data:
        min_value = INF

        for b in data:
            if a == b:
                continue
            else:
                if min_value > data[a][b] and not b in visited:
                    min_value = data[a][b]
        visited.append(a)

        result.append(min_value)
    print(result)


solved()

