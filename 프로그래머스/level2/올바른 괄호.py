def solution(a):
    s = []

    for i in range(len(a)):
        if a[i] == ")" and len(s) > 0 and s[-1] == '(':
            s.pop()
        else:
            s.append(a[i])

    if len(s) == 0:
        return True
    else:
        return False
