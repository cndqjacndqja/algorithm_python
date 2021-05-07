from _collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result_list = []
    result = 0

    if not q:
        result = 1
    while q:
        if len(q) > 1:
            result = 1
            break
        node = q.popleft()
        result_list.append(node)

        for i in data[node]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
            elif indegree[i] < 0:
                result = 1
                break

    if result > 0 or len(result_list) < n:
        print("IMPOSSIBLE")
    else:
        print(*result_list)



for _ in range(int(input())):
    n = int(input())
    initial_data = list(map(int, input().split()))
    data = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            data[initial_data[i]].append(initial_data[j])
            indegree[initial_data[j]] += 1

    change_num = int(input())
    for _ in range(change_num):
        a, b = map(int, input().split())
        flag = True
        for i in data[a]:
            if i == b:
                data[a].remove(b)
                data[b].append(a)
                indegree[b] -= 1
                indegree[a] += 1
                flag = False

        if flag:
            data[b].remove(a)
            data[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1

    topology_sort()
