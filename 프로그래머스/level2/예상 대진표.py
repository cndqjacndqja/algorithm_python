# 크기는 // 2 만큼 각 라운드 마다 감소한다.
# 각 위치는 현재 위치에 //2 + 1한 값이 인덱스가 된다.
# 그러다가 둘이 맡붙는 순간이 언제가 되는지 구해보자.

#범수 :  +1 하고 나누기 2를 했음


def solution(n, a, b):
    idx_a = a
    idx_b = b
    count = 0

    while True:
        idx_a = (idx_a + 1) // 2
        idx_b = (idx_b + 1) // 2
        count += 1

    # 만약 두개가 1차이나는데,
    # 붙으려면 조건이 어떻게 되지??
    # 두 값이 같아야 한다. 왜?

        if idx_a == idx_b:
            return count