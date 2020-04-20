def insertion_sort(seq):
    length = len(seq)
    for i in range(0, length):
        if seq[0] > seq[i]:
            seq[0], seq[i] = seq[i], seq[0]
        for j in range(i, 0, -1):
            if seq[i] < seq[j]:
                seq[j], seq[i] = seq[i], seq[j]
        print(seq)
    return seq


def test_insertion_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert (insertion_sort(seq) == sorted(seq))
    print("테스트 통과")


if __name__ == "__main__":
    test_insertion_sort()
