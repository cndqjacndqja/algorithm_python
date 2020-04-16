class Queue(object):
    def __init__(self):self.items = []
    def isEmpty(self): return not bool (self.items)
    def enqueue(self, item): self.items.insert(0, item)
    def dequeue(self):
        value = self.items.pop()
        if value is not None: return value
        else: print("큐가 비었습니다.")
    def size(self): return len(self.items)
    def peek(self):
        if self.items: return self.items[-1]
        else: print("큐가 비었습니다.")

if __name__ == "__main__":
    queue = Queue()
    for i in range(10): queue.enqueue(i)
    for i in range(10): print(queue.dequeue())
