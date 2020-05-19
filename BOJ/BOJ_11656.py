if __name__ =="__main__":
    test = input()
    testList = []
    for i in range(0, len(test)):
        testList.append("")

    result = []

    for i in range(0, len(test)):
        for j in range(i, len(test)):
            testList[i] += test.__getitem__(j)

    result = sorted(testList)

    for i in range(0, len(testList)):
        print(result[i], end="\n")


