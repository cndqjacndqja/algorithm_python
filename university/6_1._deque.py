class Queue(object):
    def __init__(self):self.items = []
    def isEmpty(self): return not bool(self.items)
    def enqueue(self, item): self.items.insert(0, item)
    def dequeue(self):
        value = self.items.pop()
        if value is not None: return value
        else: print("Queue is Empty")
    def size(self): return len(self.items)
    def peek(self):
        if self.items: return self.items[-1]
        else: print("Queue is Empty")
class Deque(Queue):
    def enqueue_back(self, item):self.items.append(item)
    def dequeue_fromt(self):
        value = self.items.pop(0)
        if value is not None: return value
        else: print("Deque is empty")
if __name__ == "__main__":
    deque = Deque()
    for i in range(10): deque.enqueue(i)

    for i in range(10): print(deque.dequeue())
