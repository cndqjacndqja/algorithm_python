a = list(input())
b = list(input())

flag = 0
def dfs(str):
    if len(str) == len(a):
        if str == a:
            print(1)
            exit()
        return

    if str[0] == 'B':
        str = str[::-1]
        str.pop()
        dfs(str)
        str.append('B')
        str = str[::-1]
    if str[-1] == 'A':
        str.pop()
        dfs(str)
        str.append('A')

dfs(b)
print(0)


