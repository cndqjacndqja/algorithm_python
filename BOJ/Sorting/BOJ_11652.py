dic = {}
for _ in range(int(input())):
    data = int(input())
    if data in dic:
        dic[data] += 1
    else:
        dic[data] = 1

print(dic.items())
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
