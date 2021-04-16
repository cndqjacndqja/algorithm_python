n = int(input())
tree = [[] for _ in range(n+1)]
wolf = ['' for _ in range(n+1)]

for i in range(2, n+1):
    ch, per, loc = input().split()
    tree[i].append(int(per))
    tree[i].append(int(loc))
    wolf[i] = ch

num = 0
def dfs(node, idx):
    global num
    if idx == 1:
        num = node[0]
        return

    if wolf[idx] == 'W':
        node[0] -= tree[idx][0]
        if node[0] <= 0:
            return 0

    dfs(node, tree[idx][1])

def solved():
    result = 0
    global num
    for i in range(2, n+1):
        if wolf[i] != 'W':
            num = 0
            dfs(tree[i], i)
            result+=num
    print(result)

solved()