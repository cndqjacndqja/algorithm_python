def decode(codes, encoded):
    dic = {}
    result = ""
    for i in codes:
        a, b = i.split("\t")
        if a == "[newline]":
            dic[b] = "\n"
        else:
            dic[b] = a
    str = ""
    for i in range(len(encoded)):
        str += encoded[i]
        if str in dic:
            result += dic[str]
            str = ""
    print(result)


if __name__ == '__main__':
    codes_count = int(input().strip())
    codes = []
    for _ in range(codes_count):
        codes_item = input()
        codes.append(codes_item)
    encoded = input()

    decode(codes, encoded)



