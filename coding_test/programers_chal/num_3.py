import heapq


def solution(a, edges):
    data = []
    count = 0
    for i in range(len(a)):
        data.append([a[i], i])
    data.sort(reverse=True, key=lambda x: x[0])
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][1] == 0:
                break
            if [data[j][1], data[i][1]] in edges or [ data[i][1], data[j][1]] in edges:
                while data[i][0] > 0:
                    count += 1
                    data[j][0] += 1
                    data[i][0] -= 1

    data.sort(reverse=True, key=lambda x: x[0])
    if data[0][0] == 0:
        print(count)
    else:
        print(-1)

solution([0,1,0] ,[[0,1],[1,2]])
