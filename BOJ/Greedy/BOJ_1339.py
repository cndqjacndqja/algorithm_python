ch = [0 for i in range(26)]

n = int(input())

data = []
for _ in range(n):
    data.append(list(input()))


for i in range(len(data)):
    for j in range(len(data[i])):
        digit = len(data[i]) - 1
        ch[ord(data[i][j]) - 65] += 10**(digit-j)


ch.sort(reverse=True)
result = 0
for i in range(26):
    result += ch[i] * (9-i)
print(result)

