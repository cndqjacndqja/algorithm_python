import time

start_time = time.time()
n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1
for c in coin:
    if c <= target:
        target += c
    else:
        break
print(target)
print(time.time() - start_time)