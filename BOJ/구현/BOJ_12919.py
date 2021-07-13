a = input()
b = input()

flag = 0
def dfs(ch, data):
    global flag
    if len(ch) == len(data):
        if ch == data:
            flag = 1
        return
    dfs(ch+'A', data)
    test = ch+'B'
    dfs(test[::-1], data)

dfs(a, b)
print(flag)