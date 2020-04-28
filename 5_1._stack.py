class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if Stack.isEmpty(self):
            print("비어있음")
            return
        else: return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    stack = Stack()
    print("스택이 비어있나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9까지 추가합니다.")
    for i in range(10): stack.push(i)
    for i in range(10): print(stack.pop())