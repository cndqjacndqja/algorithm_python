data = input()
stack = ""
check = ["U", "C", "P", "C"]
idx = 0
for i in range(len(data)):
    if data[i] == check[idx]:
        stack += data[i]
        idx += 1
    if idx == 4:
        break

if stack == "UCPC" and len(stack) == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
