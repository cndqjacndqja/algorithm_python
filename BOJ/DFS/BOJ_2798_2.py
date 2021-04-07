from itertools import permutations

def solved():
    n, m =map(int, input().split())
    data = list(map(int, input().split()))
    per_data = permutations(data, 3)
    sum_result = int(1e9)
    for i in per_data:
        if sum(i) <= m:
            sum_result = min(sum_result, abs(m - sum(i)))
    print(m - sum_result)

solved()
