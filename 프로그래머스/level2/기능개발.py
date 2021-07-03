# def solution(progresses, speeds):
#     result = []
#     time = 0
#     count = 0
#
#     while len(progresses) > 0:
#         if(progresses[0] + time * speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 result.append(count)
#                 count = 0
#             time += 1
#     result.append(count)
#     return result

def up_num(a, b):
    num1 = a / b
    num2 = a // b
    if num1 > num2:
        return int(num1) + 1
    else:
        return num2


def solution(progresses, speeds):
    day = up_num(100 - progresses[0], speeds[0])
    cnt = 1
    result = []
    for i in range(1, len(progresses)):
        expect_day = up_num(100 - progresses[i], speeds[i])
        if expect_day > day:
            result.append(cnt)
            day = expect_day
            cnt = 1
        else:
            cnt += 1

    result.append(cnt)
    print(result)

# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
#
# solution([93, 30, 55], [1, 30, 5])

solution([1, 2], [2, 1])
99 // 2
50


