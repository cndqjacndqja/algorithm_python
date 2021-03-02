result = 0
for _ in range(int(input())):
    check = []
    data = list(input())
    len_data = 0
    result_bool = True
    while len_data < len(data):
        check_data = data[len_data]
        if check_data in check:
            result_bool = False
        check.append(check_data)

        while len_data + 1 < len(data) and data[len_data + 1] == check_data:
            len_data += 1

        len_data += 1

    if result_bool:
        result += 1

print(result)
