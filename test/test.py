def solution(p, s):
    idx = 0
    count = 0
    result = 0

    for i in range(len(s)):
        if p[idx] == s[i]:
            idx += 1
            if idx == len(p):
                idx %= (len(p))
                result += 1
        else:
            count += 1

    count += idx

    if result > 0:
        return count
    else:
        return -1


print(solution("101", "10100010101101100"))
