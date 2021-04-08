from itertools import combinations  # 조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]

# 조합으로 가능한 팀 생성해주기
possible_team = list(combinations(members, N // 2))
min_stat_gap = 10000  # 갭이 가장 작은 값을 찾기 위하여
for i in possible_team:
    team1 = i
    team1_sum = 0
    for j in range(len(i)):
        member = team1[j]
        for k in team1:
            team1_sum += S[member][k]

    team2 = list(set(members) - set(i))
    team2_sum = 0
    for j in range(len(i)):
        member = team2[j]
        for k in team2:
            team2_sum += S[member][k]
    min_stat_gap = min(min_stat_gap, abs(team1_sum - team2_sum))

print(min_stat_gap)
