while True:
    try:
        n, k = map(int, input().split())
        result = n
        while n // k:
            result += n // k
            n = n // k + n % k
        print(result)
    except:
        break
