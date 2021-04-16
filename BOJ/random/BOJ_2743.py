import string

if __name__ =="__main__":
    list_lower = ".".join(string.ascii_lowercase).split(".")
    list_upper = ".".join(string.ascii_uppercase).split(".")
    test = ".".join(input()).split(".")

    for i in range(0, len(test)):
        if 97 <= ord(test[i]) <= 122:
            for j in range(0, len(list_lower)):
                if test[i] is list_lower[j]:
                    test[i] = list_lower[(j+13) % 26]
                    break

        elif 65 <= ord(test[i]) <= 99:
            for j in range(0, len(list_upper)):
                if test[i] is list_upper[j]:
                    test[i] = list_upper[(j+13) % 26]
                    break

    for i in range(0, len(test)):
        print(test[i], end="")