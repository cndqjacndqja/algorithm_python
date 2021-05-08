from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def solution(places):
    global flag
    result = []
    for data in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if data[i][j] == 'P':
                    if not check(i, j, data):
                        flag = False
        if flag:
            result.append(1)
        else:
            result.append(0)


    return result



def check(x, y, data):
    q = deque()
    visited = [[False for _ in range(5)] for _ in range(5)]
    q.append((x, y))
    visited[x][y] = True

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                range_num = abs(x-nx) + abs(y-ny)
                if data[nx][ny] == 'O' and range_num <= 2:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                if data[nx][ny] == 'P' and range_num <= 2:
                    return False

    return True

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])