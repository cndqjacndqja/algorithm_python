from string import ascii_lowercase
import sys

if __name__ == "__main__":
    list = list(ascii_lowercase)
    test = input()
    temp = []

    result = []
    for i in range(0, len(list)):
        result.append(-1)

    for i in range(0, len(test)):
        for j in range(0, len(list)):
            if list[j] == test[i]:
                if not test[i] in temp:
                    result[j] = i
                    temp.append(test[i])


    for i in range(0, len(result)):
        print(result[i], end =' ')