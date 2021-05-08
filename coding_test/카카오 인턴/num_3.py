def check(data, result, n):
    result_data = ""
    for i in range(n):
        if data[i] in result:
            result_data+="O"
        else:
            result_data += "X"
    return result_data

def solution(n, k, cmd):
    data = [i for i in range(n)]

    q = []
    mouse = k

    for com in cmd:
        if com[0] == "D":
            mouse = (mouse + int(com[2])) % len(data)
        elif com[0] == "C":
            pop_data = data.pop(mouse)
            q.append((pop_data, mouse))
            if mouse == len(data):
                mouse -= 1
        elif com[0] == "U":
            mouse -= int(com[2])
            if mouse < 0:
                mouse += len(data)
        elif com[0] == "Z":
            if len(q) > 0:
                node, now = q.pop()
                data.insert(now, node)
                if now < mouse:
                    mouse += 1

    return check([i for i in range(n)], data, n)