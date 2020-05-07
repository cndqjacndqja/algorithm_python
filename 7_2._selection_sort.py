def selection_sort(seq):
    length = len(seq)
    for i in range(0, length - 1):
        for j in range(i, length):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
        print(seq)
    return seq


def selection(seq):

    for i in range(0, len(seq) -1):
        for j in range(i, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq

def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert (selection_sort(seq) == selection(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_selection_sort()
