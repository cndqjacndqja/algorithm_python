n = int(input())

start_data = []
end_data = []
for _ in range(n):
    st = list(input())
    data1 = list(''.join(st[0:5]).split(":"))
    data2 = list(''.join(st[8:13]).split(":"))
    start_data.append(data1)
    end_data.append(data2)

start_data.sort(reverse=True, key=lambda x:(x[0], x[1]))
end_data.sort(key=lambda x:(x[0], x[1]))

if start_data[0][0] > end_data[0][0]:
    print(-1)
elif start_data[0][0] == end_data[0][0] and start_data[0][1] > end_data[0][1]:
    print(-1)
else:
    print("{0}:{1} ~ {2}:{3}".format(start_data[0][0], start_data[0][1], end_data[0][0], end_data[0][1]))