n = int(input())
tmp = n % 8

if tmp == 0:
    print(2)
elif tmp >= 5:
    print(10-tmp)
else:
    print(tmp)