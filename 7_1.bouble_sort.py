def bouble_sort(seq):
    length = len(seq)
    for num in range(length-1, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
        print(seq)
    return seq


def test_bouble_sort():
    seq = [11, 3, 28, 43 , 9 , 4]
    assert(bouble_sort(seq) == sorted(seq))
    print("테스트 통과!")

if __name__ == "__main__":
    test_bouble_sort()