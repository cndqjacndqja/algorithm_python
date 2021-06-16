from _collections import deque
import heapq
from heapq import heappush, heappop


def main():
    for t in range(int(input())):
        other_side = []
        n = int(input())
        data = list(map(int, input().split()))
        data.sort()

        q = []
        result = 0
        if len(data) < 2:
            result += data.pop()
        else:
            a = data.pop(0)
            b = data.pop(0)
            heappush(other_side, a)
            heappush(other_side, b)
            result += max(a, b)

            for i in data:
                heappush(q, -i)
            while q:
                pop_data = heappop(other_side)
                result += pop_data
                heappush(q, -pop_data)

                a = -heappop(q)
                b = -heappop(q)
                heappush(other_side, a)
                heappush(other_side, b)
                result += max(a, b)

        print("#{0} {1}".format(t + 1, result))


main()
