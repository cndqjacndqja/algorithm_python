import copy
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def solved():
    temp = [list(map(int, input().split()))]
    data = [[[None, None] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            data[i][j][0], data[i][j][1] = temp[i][j * 2], temp[i][j * 2 + 1] - 1

def food(now_x, now_y, data):
    position = []
    for i in range(1, 4):
        nx, ny = now_x+dx[data[now_x][now_y][1]], now_y+dy[data[now_x][now_y][1]]
        if 0<=nx<4 and 0<=ny<4 and 1 <= data[nx][ny][0] <= 16:
            position.append([nx, ny])
        now_x, now_y = nx, ny
    return position


def find_fish(data, index):

    for i in range(4):
        for j in range(4):
            if data[i][j][0] == index:
                return [i, j]
    return None




