zero = []
one = []

data = list(map(int, input()))

start_idx = 0
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        if data[i-1] == 0:
            zero.append((start_idx, i-1))
        else:
            one.append((start_idx, i-1))
        start_idx = i
    if i == len(data)-1:
        if data[i] == 0:
            zero.append((start_idx, i))
        else:
            one.append((start_idx, i))

if len(zero) < len(one):
    print(len(zero))
else:
    print(len(one))


