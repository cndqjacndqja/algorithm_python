from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
rotate_x, rotate_y = [1, 0], [0, 1]


def solution(board):
    q = deque()
    q.append([0, 0, 0, 1])
    n = len(board)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    while q:
        x1, y1, x2, y2 = q.popleft()

        for i in range(4):
            nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and not visited[nx1][ny1] and not visited[nx2][ny2]:
                    q.append((nx1, ny1, nx2, ny2))
                    visited[nx1][ny1] = True
                    visited[nx2][ny2] = True

        if y1 == y2:
            for d in [-1, 1]:
                if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                    q.append((x2, y2, x1+d, y1+d))