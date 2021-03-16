import heapq

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

heapq.heapify(data)
result = []
while len(data) > 1:
    num1 = heapq.heappop(data)
    num2 = heapq.heappop(data)
    heapq.heappush(data, num1+num2)
    result.append(num1+num2)

print(sum(result))
