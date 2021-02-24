import heapq

q = []

for _ in range(int(input())):
    heapq.heappush(q, int(input()))

result = 0
while len(q) > 1:
    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)
    heapq.heappush(q, (num1 + num2))
    result += num1+num2

print(result)