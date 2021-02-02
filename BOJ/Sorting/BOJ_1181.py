n = int(input())
data = []

for _ in range(n):
    word = input()
    count = len(word)
    data.append((word, count))

data = list(set(data))

data.sort(key=lambda x: (x[1],x[0]))
for i in data:
    print(i[0])