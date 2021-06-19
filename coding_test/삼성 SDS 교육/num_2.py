a, b, L, filter_data = 0, 0, 0, 0,

def calculator(idx):
    global filter_data, a, b
    for i in range(len(filter_data)):
        if filter_data[i] == '0':
            continue
        elif filter_data[i] == '+':
            a[idx + i] += 1
        else:
            a[idx + i] -= 1


def reverse_calculator(idx):
    global filter_data, a, b
    reverse_filter = filter_data[::-1]
    for i in range(len(reverse_filter)):
        if reverse_filter[i] == '0':
            continue
        elif reverse_filter[i] == '+':
            a[idx + i] += 1
        else:
            a[idx + i] -= 1

def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
def main():
    global a, b, L, filter_data
    for _ in range(int(input())):
        a, b, L = input().split()
        a = list(''.join(a))
        a = list(map(int, a))
        b = list(''.join(b))
        b = list(map(int, b))
        filter_data = list(input())
        # 0 추가하기
        for i in range(len(a), 6):
            a.insert(0, 0)
        for i in range(len(b), 6):
            b.insert(0, 0)

        ## 이제 차례대로 필터 적용하기
        flag = True
        count = 0
        for i in range(6):
            # 먼저 이게 맞는지
            if a[i] == b[i]:
                continue
            else:
                while a[i] > b[i]:
                    if filter_data[0] == '-':
                        calculator(i)
                        count += 1
                    if filter_data[-1] == '-':
                        reverse_calculator(i)
                        count += 1
                    else:
                        break
                while a[i] < b[i]:
                    if filter_data[0] == '+':
                        count+=1
                        calculator(i)
                    elif filter_data[-1] == '+':
                        reverse_calculator(i)
                        count += 1
                    else:
                        break
        if check(a, b):
            print(count)
        else:
            print(-1)

main()

