data = input()
left = len(data) // 2
right = left

if sum([int(i) for i in data[:left]]) == sum([int(i) for i in data[right:]]):
    print("LUCKY")
else:
    print("READY")
