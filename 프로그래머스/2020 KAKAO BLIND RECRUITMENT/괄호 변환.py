from _collections import deque


def find_balance(data):
    length = len(data)

    if length == 0:
        return 0
    q = []

    for i in range(len(data)):
        if data[i] == '(':
            q.append('(')
        elif data[i] == ')':
            if q[-1] == '(':
                q.pop()
            else:
                q.append(')')

    if len(data) == 0:
        return 1  # 참 -> 올바른 괄호 문자열
    else:
        return 2  # 거짓 -> 균형잡힌 괄호 문자열


def solution(p):
    answer = ''
    return answer
