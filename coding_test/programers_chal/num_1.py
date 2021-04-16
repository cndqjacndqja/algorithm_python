def solution(absolutes, signs):
    sum_data = 0
    for i in range(len(absolutes)):
        if signs[i]:
            sum_data += absolutes[i]
        else:
            sum_data -= absolutes[i]

    print(sum_data)

solution([4, 7, 12], [True,False,True])
