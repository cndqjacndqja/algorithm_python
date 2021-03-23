from _collections import deque

n = int(input())
t = [0 for _ in range(15)]
p = [0 for _ in range(15)]
for i in range(n):
    t[i], p[i] = map(int, input().split())

result = []
for i in range(n):
    q = deque()
    q.append(i)

    max_num = 0
    while q:
        pop_data = q.popleft()
        if pop_data


        for i in range(pop_data, n):

