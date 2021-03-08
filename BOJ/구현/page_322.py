data = input()

data1 = []
data2 = []
for i in data:
    if 65 <= ord(i) <= 90:
        data1.append(i)
    else:
        data2.append(int(i))

data1.sort()
for i in data1:
    print(i,end='')
print(sum(data2),end='')