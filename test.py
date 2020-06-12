def permutation(n, r):
    num = 1
    for i in range(n, r-1, -1):
        num *= i
    return num

def test(v = 10, v2 = 20 , *v3):
    pass
if __name__ == "__main__":

    print("총 데이터의 갯수를 입력하시오")
    n = int(input())

    print("입력한 데이터 중 몇개의 데이터를 선택할 것인지 입력하시오.")
    r = int(input())

    print(permutation(n, r))

    test(1,2,3,4,5)


