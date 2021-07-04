from itertools import combinations

number = [1, 1, 1, 1, 1]
target = 3

score = 0

def dfs(sum, idx):
    global number, score
    if idx == len(number):
        if sum == target:
            score += 1
        return 0
    dfs(sum+number[idx], idx+1)
    dfs(sum-number[idx], idx+1)



def solution(numbers, target):
    dfs(0, 0)
    return score

solution(number, target)