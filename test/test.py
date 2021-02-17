input_list = input().split()
N = int(input_list[0])
M = int(input_list[1])
input_list_2 = input().split()
line_list = []
line_max = 0
for i in range(N):
    line_list.append(int(input_list_2[i]))
    line_max = max(line_max, line_list[i])                          #input 처리 과정; 동시에 최댓값을 탐색

def find_length(upper_length, lower_length, need_length):
    upper = upper_length
    lower = lower_length
    best_length = 0
    while (upper >= lower):
        mid = (upper + lower) // 2
        cur_sum = 0
        for i in range(N):                                          #현재 높이에서 자를 경우 얼마만큼의 나무를 가져갈 수 있을지 계산
            if line_list[i] > mid:
                cur_sum += line_list[i] - mid
            if cur_sum > need_length:
                break
        if cur_sum >= need_length:                                  #필요한 만큼 혹은 그 이상 잘라낸 경우; 더 높이 잘라도 됨
            lower = mid + 1
            if mid > best_length:                                   #만약 현재의 값이 최댓값이면 일단 이 값을 저장
                best_length = mid
        else:                                                       #너무 적게 잘라낸 경우; 더 낮게 잘라야 함
            upper = mid - 1
    return best_length

print(find_length(line_max, 1, M))   