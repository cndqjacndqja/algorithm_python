n, m, e = map(int, input().split())
# 길이

data1 = []

data1_pi = []


data2 = []
data2_pi = []
data1_cnt = 0
data2_cnt = 0

input_dis = list(map(int, input().split()))

for dis in input_dis:
    discount = m - dis
    if discount < 0:
        data1.append(discount * -1)
    elif discount > 0:
        data2.append(discount)

data1_test_cnt = len(data1)
for i in range(len(data1)):
    data1_pi.append(data1_test_cnt)
    data1_test_cnt -= 1

data2_test_cnt = len(data2)
for i in range(len(data2)):
    data2_pi.append(data2_test_cnt)
    data2_test_cnt -= 1

result = 0
for i in range(len(data1)):
    if data1_pi[i] == m:
        result = data1[i]

for i in range(len(data2)):
    if data2_pi[i] == m:
        result = min(result, data2[i])

print(result)



