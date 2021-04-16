import heapq


def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    for i in edges:
        x, y = i
        tree[x].append(y)
        tree[y].append(x)
    data = []
    data_a = []

    for i in range(len(a)):
        data.append([a[i], i])
        data_a.append([a[i], i])
    data.sort(reverse=True, key=lambda x:x[0])
    count = 0
    for i in range(len(a)):
        if a[data[i][1]] == 0:
            continue
        for j in tree[data[i][1]]:
            while a[data[i][1]] > 0 and a[j] != 0:
                count += 1
                a[data[i][1]] -= 1
                a[j] += 1

    if count == 0:
        return -1
    else:
        return count




print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
