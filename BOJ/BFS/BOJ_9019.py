from _collections import deque

dx = ['D', 'S', 'L', 'R']


def solve():

    for _ in range(int(input())):
        a, b = map(int, input().split())
        result = ['' for _ in range(10001)]
        visited = [False for _ in range(10001)]
        q = deque()
        q.append(a)
        visited[a] = True

        while q:
            pop_data = q.popleft()
            if pop_data == b:
                break

            D = pop_data * 2 % 10000
            if not visited[D] and result[D] == '':
                result[D] = result[pop_data] + 'D'
                visited[D] = True
                q.append(D)
            S = pop_data - 1 if pop_data != 0 else 9999
            if not visited[S] and result[S] == '':
                result[S] = result[pop_data] + 'S'
                visited[S] = True
                q.append(S)

            L = pop_data % 1000 * 10 + pop_data // 1000
            if not visited[L] and result[L] == '':
                result[L] = result[pop_data] + 'L'
                visited[L] = True
                q.append(L)

            R = pop_data % 10 * 1000 + pop_data // 10
            if not visited[R] and result[R] == '':
                result[R] = result[pop_data] + 'R'
                visited[R] = True
                q.append(R)

        print(result[b])


solve()
