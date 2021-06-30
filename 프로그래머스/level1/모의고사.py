def solution(answers):
    num1_list = [1, 2, 3, 4, 5]
    num2_list = [2, 1, 2, 3, 2, 4, 2, 5]
    num3_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for idx, i in enumerate(answers):
        if num1_list[idx % 5] == i:
            score[0] += 1
        elif num2_list[idx % 8] == i:
            score[1] += 1
        elif num3_list[idx % 10] == i:
            score[2] += 1

    result = []
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result
