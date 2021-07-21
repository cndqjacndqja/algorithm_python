from _collections import deque

n = int(input())
data = [[] for _ in range(n+1)]

for i in range(1, n+1):
    str = list(map(int, input().split()))
    for j in range(len(str)-1):
        data[i].append(str[j])

m = int(input())
virus = list(map(int, input().split()))

q = deque()

visited = [-1 for _ in range(n+1)]
check = [False for _ in range(n+1)]

for i in virus:
    q.append((i, 0))
    visited[i] = 0
    check[i] = True


while q:
    pop_x, cnt = q.popleft()
    visited[pop_x] = cnt


    for i in data[pop_x]:
        if not check[i]:
            check_cnt = 0
            for j in data[i]:
                if check[j]:
                    check_cnt+=1
            if len(data[i])/2 <= check_cnt:
                q.append((i, cnt+1))
                check[i] = True

for i in range(1, n+1):
    print(visited[i], end=' ')

