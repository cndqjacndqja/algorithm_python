import copy

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]


def spread_virus(start_x, start_y):
    spread_data = copy.deepcopy(data)
    