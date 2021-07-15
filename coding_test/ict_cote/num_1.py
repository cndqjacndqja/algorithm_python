def maxTickets(tickets):
    tickets.sort()
    count = 1
    result = []
    element = []
    for i in tickets:
        if len(element) < 1:
            element.append(i)
        else:
            if abs(element[-1] - i) <= 1:
                element.append(i)
                count += 1
            else:
                result.append(count)
                count = 1
                element.clear()
                element.append(i)
    return max(result)


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input().strip()))

    print(maxTickets(data))