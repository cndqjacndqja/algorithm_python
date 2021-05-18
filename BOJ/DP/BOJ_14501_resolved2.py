n = int(input())
p = [0 for _ in range(n + 1)]
t = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    a, b = map(int, input().split())
    p[i] = a
    t[i] = b

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    idx = i + p[i] - 1
    if idx <= n:
        dp[idx] = max(max(dp[0:i]) + t[i], dp[idx])

print(dp)


# 여기서 그럼 dp를 뭐라고 정의해야 할까,,? 해당까지의 최대 값??
# 근데 그렇게 표현하기가 묘한게, i+p[i]의 값이 범위 안에 있어야 갱신이 된다.
# 내가 이 문제를 풀면서 어려웠던 점은, 나는 변수의 역할을 딱 지정하면서 생각하는 편인데 dp를 뭐라고 정의하기가
# 좀 그렇다. 그래도 나름대로 정의를 해보자면,,, 해당 범위까지의 가질 수 있는 최댓 값의 모임.
# 아,,, 이렇게 정의하면 안되네...
