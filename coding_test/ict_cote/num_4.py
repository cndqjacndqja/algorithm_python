def maxEvents(arrival, duration):
    data = []
    for i in range(len(arrival)):
        data.append([arrival[i], duration[i]+arrival[i]])
    data.sort(key=lambda x: (x[1], x[0]))
    result = 1
    standard = data[0][1]
    for i in range(1, n):
        if standard <= data[i][0]:
            result += 1
            standard = data[i][1]
    print(result)


if __name__ == '__main__':
    n = int(input())
    arrival = []
    for _ in range(n):
        arrival.append(int(input().strip()))

    n = int(input())
    duration = []
    for _ in range(n):
        duration.append(int(input().strip()))
    maxEvents(arrival, duration)