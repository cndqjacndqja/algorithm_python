import sys
arr= sys.stdin.readline().replace('\n','')
m=int(sys.stdin.readline())
idx = len(arr)

for _ in range(m):
    val = input()
    if val == 'L':
        if idx !=0:
            idx -= 1
    elif val == 'D':
        if idx != len(arr):
            idx += 1
    elif val == 'B':
        if idx !=0:
            tmp = arr[:idx-1] + arr[idx:]
            arr = tmp
            idx -= 1
    else: #P $
        p = val[2]
        tmp = arr[:idx] + p + arr[idx:]
        arr = tmp
        idx += 1
print(arr)