
def min_coin_count(value, list):
    count = 0
    list.sort(reverse=True)
    for i in list:
        c = value // i
        value -= c * i
        count += c
    return count


if __name__=="__main__":
    list = [1, 10, 50, 500, 100]
    print(min_coin_count(940, list))
