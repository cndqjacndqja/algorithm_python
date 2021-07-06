from heapq import heappush, heappop, heapify


def calcul(a, b):
    return a + (b * 2)


def solution(scoville, K):
    heapify(scoville)
    count = 0

    while scoville:
        a = heappop(scoville)
        if a < K:
            if len(scoville) < 1:
                return -1
            b = heappop(scoville)
            count += 1
            heappush(scoville, calcul(a, b))

    return count


print(solution([1, 2, 3, 9, 10, 12],	7))