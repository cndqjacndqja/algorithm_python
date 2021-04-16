import sys

class Deque():
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if len(self.items) == 0:
            print(-1)
        else: print(self.items.pop(0))

    def pop_back(self):
        if len(self.items) == 0:
            print(-1)
        else: print(self.items.pop(len(self.items)-1))

    def size(self):
        print(len(self.items))

    def empty(self):
        if len(self.items) == 0:
            print(1)
        else: print(0)

    def front(self):
        if len(self.items) == 0:
            print(-1)
        else: print(self.items[0])

    def back(self):
        if len(self.items) == 0:
            print(-1)
        else: print(self.items[-1])


if __name__ == "__main__":
    N = int(input())
    deq = Deque()

    for i in range(0, N):
        cmd = sys.stdin.readline().split()

        if cmd[0] == "push_front":
            deq.push_front(int(cmd[1]))
        elif cmd[0] == "push_back":
            deq.push_back(int(cmd[1]))
        elif cmd[0] == "pop_front":
            deq.pop_front()
        elif cmd[0] == "pop_back":
            deq.pop_back()
        elif cmd[0] == "size":
            deq.size()
        elif cmd[0] == "empty":
            deq.empty()
        elif cmd[0] == "front":
            deq.front()
        elif cmd[0] == "back":
            deq.back()

