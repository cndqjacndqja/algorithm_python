from _collections import deque

def max_calcul(q):
    test = max([x[0] for x in q])
    return test

def solution(priorities, location):
    s = {}
    q = deque()
    count = 1
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    while q:
        pop_data, idx = q.popleft()
        if len(q) > 0 and max_calcul(q) > pop_data:
            q.append((pop_data, idx))
        else:
            s[idx] = count
            count += 1
    print(s[location])


solution([1, 1, 9, 1, 1, 1]	,0)
