import copy


def solution(rows, columns, queries):
    data = []
    count = 1
    for i in range(columns):
        data_insert = []
        for j in range(rows):
            data_insert.append(count)
            count += 1
        data.append(data_insert)
    result = []
    for q in queries:
        x1, y1, x2, y2 = q
        data, min_value = move(x1, y1, x2, y2, data)
        result.append(min_value)
    return result



def move(y1, x1, y2, x2, data):
    copy_data = copy.deepcopy(data)
    min_value = 1e9

    for y in range(y1 - 1, y2):
        if y == y1 - 1:
            for x in range(x1 - 1, x2 - 1):
                copy_data[x][y] = data[x + 1][y]
                min_value = min(min_value, data[x + 1][y])
            copy_data[x2 - 1][y1 - 1] = data[x2 - 1][y1]
            min_value = min(min_value, data[x2 - 1][y1])
        elif y == y2 - 1:
            for x in range(x1, x2):
                copy_data[x][y] = data[x - 1][y]
                min_value = min(min_value, data[x - 1][y])
            copy_data[x1 - 1][y2 - 1] = data[x1 - 1][y2 - 2]
            min_value = min(min_value, data[x1 - 1][y2 - 2])
        else:
            copy_data[x1 - 1][y] = data[x1 - 1][y - 1]
            min_value = min(min_value, data[x1 - 1][y - 1])
            copy_data[x2 - 1][y] = data[x2 - 1][y + 1]
            min_value = min(min_value, data[x2 - 1][y + 1])

    return copy_data, min_value


solution(100,	97,	[[1,1,100,97]])