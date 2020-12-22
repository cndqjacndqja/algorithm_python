a, k = map(int, input().split(" "))
count = 0

while a != 1:
    if a % k == 0:
        a /= k
        count += 1
    else:
        a -= 1
        count += 1
print(count)