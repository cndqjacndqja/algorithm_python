import sys

from heapq import heappush, heappop

n = int(input())
q = []

for _ in range(n):
    com = int(sys.stdin.readline())
    if com == 0:
        if len(q) <= 0:
            print(0)
        else:
            print(heappop(q))
    else:
        heappush(q, com)
