class Stack(object):
    def __init__(self): self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("is Empty!")
        else:
            return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items is not None:
            return self.items[-1]

        else:
            print("is Empty")

