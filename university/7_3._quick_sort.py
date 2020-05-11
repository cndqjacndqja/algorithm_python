def partition(seq, start, end):
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot: left += 1
        while left <= right and pivot < seq[right]:
            right -= 1
        if right < left: done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]
    print(seq)
    return right


def quick_sort(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot - 1)
        quick_sort(seq, pivot + 1, end)
    return seq


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print("\n")
    assert (quick_sort(seq, 0, len(seq)-1) == sorted(seq))
    print("테스트 통과!\n")


if __name__ == "__main__":
    test_quick_sort()
