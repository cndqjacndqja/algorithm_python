

data = input()
index = len(data)
for _ in range(int(input())):
    com = list(input().split())
    comm = com[0]
    if comm == "L":
        if not index == 0:
            index -= 1

    elif comm == "D":
        if index != len(data):
            index += 1

    elif comm == "B":
        if index != 0:
            temp = data[:index-1] + data[index:]
            data = temp
            index -= 1

    elif comm == "P":
        temp = data[0:index] + com[1]+ data[index:]
        data = temp
        index += 1
print(data)
