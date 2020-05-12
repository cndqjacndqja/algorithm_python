import sys

if __name__ == "__main__":
    a = sys.stdin.readline().split(" ")
    n = int(a[0])
    k = int(a[1])
    result = []

    index = k-1
    seq = [i for i in range(1, n + 1)]

    for i in range(0, n):
        if index >= len(seq):
            index = index % len(seq)
        result.append(str(seq.pop(index)))
        index += k - 1
    print("<"+", ".join(result)+">")