def solution(N, stages):
    data = []
    index = 0
    stages.sort()
    count = 0
    for i in range(1, N + 1):
        index += count
        count = 0
        for j in range(index, len(stages)):
            if stages[j] == i:
                count += 1
        if len(stages) - index != 0:
            data.append([i, count / (len(stages) - index)])
        elif len(stages) - index == 0:
            data.append([i, count])

    data.sort(key=lambda x: (-x[1], x[0]))

    result = []
    for i in data:
        result.append(i[0])
    return result


solution(4, [4, 4, 4, 4, 4])
