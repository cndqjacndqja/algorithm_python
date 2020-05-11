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


def reverse_string_with_stack(str):
    s = Stack()

    reverse_str = ""
    for i in range(0, len(str)):
        s.push(str[i])

    for i in range(0, s.size()):
        reverse_str += s.pop()

    print(reverse_str)


if __name__ == "__main__":
    reverse_string_with_stack("나는 조충범이다.")