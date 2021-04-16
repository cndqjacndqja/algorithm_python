from _collections import deque


def solution(s):
    count = 0
    for i in range(len(s) - 1):
        if find(s[i:len(s)] + s[:i]):
            count += 1
    print(count)


def find(data):
    q = []

    for i in range(len(data)):
        if data[i] == ']':
            if len(q) > 0 and q[-1] == '[':
                q.pop()
            else:
                q.append(data[i])
        if data[i] == ')':
            if len(q) > 0 and q[-1] == '(':
                q.pop()
            else:
                q.append(data[i])
        if data[i] == '}':
            if len(q) > 0 and q[-1] == '{':
                q.pop()
            else:
                q.append(data[i])
        elif data[i] == '[' or data[i] == '(' or data[i] == '{':
            q.append(data[i])

    if len(q) == 0:
        return True
    else:
        return False


solution("}}}")
