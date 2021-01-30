data = list(input())

dir = [[i, 0] for i in range(26)]

for i in range(len(data)):
    data_chr = ord(data[i])
    if 97 <= data_chr <= 122:
        dir[data_chr - 97][1] += 1
    elif 65 <= data_chr <= 90:
        dir[data_chr - 65][1] += 1

dir.sort(reverse=True, key=lambda x: x[1])
if dir[0][1] == dir[1][1]:
    print("?")
else:
    print(chr(dir[0][0] + 65))
