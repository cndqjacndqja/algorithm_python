import copy

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

# 바이러스 퍼트리기
def spread_virus(start_x, start_y):
    spread_data = copy.deepcopy(data)
    