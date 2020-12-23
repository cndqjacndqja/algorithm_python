n = int(input())

status = [1 for _ in range(2)]


def right():
    if status[1] < n:
        status[1] += 1


def left():
    if status[1] > 1:
        status[1] -= 1


def up():
    if status[0] > 1:
        status[0] -= 1


def down():
    if status[0] < n:
        status[0] += 1


cmd = input().split(" ")
for i in cmd:
    if i == "R":
        right()
    elif i == "L":
        left()
    elif i == "U":
        up()
    elif i == "D":
        down()

print(status[0], status[1])
