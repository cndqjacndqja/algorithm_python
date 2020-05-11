
def swap(a, b):
    temp = a
    a = b
    b = temp


if __name__ == "__main__":
    a = 456
    b = 123

    temp = a
    a = b
    b = temp
    print(a, b)