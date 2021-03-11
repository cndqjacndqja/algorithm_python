def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    s = [p[0]]

    for i in range(1, len(p)):
        if p[i] == '(':
            s.append(p[i])
        else:
            if len(s) > 0 and s[-1] == '(':
                s.pop()
            else:
                s.append(p[i])

    if len(s) == 0:
        return True
    else:
        return False



def solution(p):

    answer = ''
    if p == '':
        return p
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        u += solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += u
    return answer

print(solution("(()())()"))



# 으아아아아 모르겠다아아