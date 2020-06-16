def permutation(n, r):
    num = 1
    m = 1
    c = 1

    if n - r is 0:
        for i in range(n, 0, -1):
            num *= i
        return num
    else:
        for i in range(n, 0, -1):
            m *= i
        for j in range(n-r, 0, -1):
            c *= j
        return m//c


if __name__ == "__main__":

    print("총 데이터의 갯수를 입력하시오")
    n = int(input())

    print("입력한 데이터 중 몇개의 데이터를 선택할 것인지 입력하시오.")
    r = int(input())

    print(permutation(n, r))



