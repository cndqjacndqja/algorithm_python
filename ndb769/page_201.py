n, m = map(int, input().split())

data = list(map(int, input().split(" ")))


def cut(data, h):
    total = 0
    for i in data:
        if i > h:
            total += i - h

    return total


max_data = max(data)

range_data = [i for i in range(max_data + 1)]


def binary_search(graph, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if cut(data, graph[mid]) == target:
        print(graph[mid])
    elif cut(data, graph[mid]) < target:
        binary_search(graph, target, start, mid - 1)
    else:
        binary_search(graph, target, mid + 1, end)


binary_search(range_data, m, 0, len(range_data) - 1)
