n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0
result = 0
stack_cnt = 0
while cnt < len(data):
    pop_data = data[cnt]
    stack_cnt += 1
    if stack_cnt == pop_data:
        stack_cnt = 0
        result += 1
    cnt += 1
print(result)


