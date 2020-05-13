from string import ascii_lowercase
import sys
if __name__ == "__main__":
    list = list(ascii_lowercase)
    test = input()
    result = []
    for i in range(0, 26):
        result.append(0)

    for i in range(0, len(test)):
        for j in range(0, len(list)):
            if test[i] == list[j]:
                result[j] += 1

    for i in range(0, len(result)):
        print(result[i], end = ' ')