def solution(n):
    num = format(n, 'b')

    arr = ",".join(str(num)).split(",")
    result = 0

    for i in range(0, len(arr)):
        if arr[i] is "1":
            num = 1
            for j in range(0, len(arr) - (i+2)):
                num *= 3

        result += num

    return result


if __name__ == "__main__":
    print(solution(4))
