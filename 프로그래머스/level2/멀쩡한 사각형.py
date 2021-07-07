def solution(w, h):
    w_data = []
    h_data = []

    for i in range(1, w+1):
        if w % i == 0:
            w_data.append(i)

    for i in range(1, h+1):
        if h % i == 0:
            h_data.append(i)

    data = set(w_data).intersection(h_data)
    return w*h - (w+h-max(data))

print(solution(244, 136))