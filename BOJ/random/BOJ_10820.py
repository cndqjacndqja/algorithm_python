if __name__ == "__main__":
    result = [0, 0, 0, 0]

    while True:

        try:
            test = ".".join(input()).split(".")
            for i in range(0, len(test)):
                if 97 <= ord(test[i]) <= 122:
                    result[0] += 1
                elif 65 <= ord(test[i]) <= 99:
                    result[1] += 1
                elif test[i] == " ":
                    result[3] += 1
                else:
                    result[2] += 1

            for i in range(0, 4):
                print(result[i], end=" ")
                result[i] = 0
            print()
        except EOFError:
            break
