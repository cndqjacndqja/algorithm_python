import sys

class Queue():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("-1")
        else:
            print(self.items.pop(0))

    def size(self):
        print(len(self.items))

    def empty(self):
        if len(self.items) == 0:
            print("1")
        else:
            print("0")

    def front(self):
        if len(self.items) == 0:
            print("-1")
        else:
            print(self.items[0])

    def back(self):
        if len(self.items) == 0:
            print("-1")
        else:
            print(self.items[-1])


if __name__ == "__main__":
    a = int(input())


    q = Queue()
    for i in range(0, a):
        command = sys.stdin.readline().split()

        if command[0] == "push":
            q.push(command[1])

        elif command[0] == "pop":
            q.pop()

        elif command[0] == "size":
            q.size()

        elif command[0] == "empty":
            q.empty()

        elif command[0] == "front":
            q.front()

        elif command[0] == "back":
            q.back()
