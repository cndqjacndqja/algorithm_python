# 과장을 한 곳에 있는 사람들은, 진실을 아는 사람이 없어야 한다.
# 과장을 들은 사람들이 진실이 있는 사람들이랑 같이 있으면 안된다.
# 과장을 들은 사람들은, 진실을 아는 사람과 절대 겹치면 안된다.


n, m = map(int, input().split())
true_member = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
check = [False for _ in range(n + 1)]


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


def solved():
    team = []
    for _ in range(m):
        data = list(map(int, input().split()))
        team.append(data)
        for i in range(1, data[0]):
            union(data[i], data[i + 1], parent)

    for i in range(true_member[0]):
        node = true_member[i + 1]
        node_parent = find(node, parent)
        for j in range(1, n + 1):
            if parent[j] == node_parent:
                check[j] = True

    result = 0
    for i in range(len(team)):
        flag = True
        for j in range(1, len(team[i])):
            if check[team[i][j]]:
                flag = False
                break
        if flag:
            result += 1
    print(result)


solved()
