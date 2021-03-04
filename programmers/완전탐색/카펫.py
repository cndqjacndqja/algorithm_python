def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_garo = yellow // i    # 가로길이
            y_sero = i              # 세로길이
            b_garo = y_garo + 2
            b_sero = y_sero

            if (b_garo * 2 + b_sero * 2) == brown and (y_garo * y_sero) == yellow:
                if not b_garo + y_garo < b_sero + y_sero:
                    return [b_garo, b_sero + 2]
