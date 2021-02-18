num = input()
broken_len = int(input())
broken_data = []
if broken_len != 0:
    broken_data = list(map(int, input().split()))

min_number = abs(100 - int(num))

for i in range(1000001):
    i_str = str(i)
    for j in range(len(i_str)):
        if int(i_str[j]) in broken_data:
            break
        elif j == len(i_str) - 1:
            min_number = min(min_number, abs(int(num) - i) + len(i_str))

print(min_number)