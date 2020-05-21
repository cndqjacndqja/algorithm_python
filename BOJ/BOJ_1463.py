if __name__ == "__main__":
    a = int(input())
    count = 0
    minimum = [a]


    def cal(a):
        list = []
        for i in a:
            list.append(i - 1)
            if i % 3 == 0:
                list.append(i / 3)

            if i % 2 == 0:
                list.append(i / 2)
        print(list)
        return list

    while True:
        if a == 1:
            print(count)
            break
        temp = minimum[:]
        minimum = []
        minimum = cal(temp)
        count += 1
        if min(minimum) == 1:

            print(count)
            break

