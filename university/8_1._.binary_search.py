def binary_search_rec(seq, target, low, high):
    if low > high:
        return None
    mid = (low +  high) // 2
    if target == seq[mid]:
        return mid
    elif target < seq[mid]:
        return binary_search_rec(seq, target, low, mid - 1)
    else:
        return binary_search_rec(seq, target, mid + 1, high)


def test_binary_search():
    seq = [1, 2, 5, 6, 7, 10, 12, 14, 15]
    target = 15
    assert (binary_search_rec(seq, target, 0, len(seq) -1) == 8)
    print("테스트 통과!")


if __name__ == "__main__":
    test_binary_search()


