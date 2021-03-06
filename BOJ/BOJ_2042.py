n, m, k = map(int, input().split())

data = []
tree = [0 for _ in range(n * 4)]


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def update(start, end, node, idx, change):
    if idx < start or idx > end:
        return

    tree[node] += change
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, idx, change)
        update(mid + 1, end, node * 2 + 1, idx, change)


def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


for _ in range(n):
    data.append(int(input()))

init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        d = c - data[b-1]
        data[b-1] = c
        update(0, n - 1, 1, b-1, d)
    elif a == 2:
        print(sum(0, n-1, 1, b-1, c-1))

