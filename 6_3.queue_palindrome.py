import  string
import collections

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self): return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty(self): print("is Empty")
        else: return self.items.pop()

    def size(self): return len(self.items)

    def peek(self):
        return self.items[-1]

    def __repr__(self): return repr(self.items)

class Dequeue(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if self.isEmpty(self): print("is Empty")
        else: return self.items.pop(0)


STRIP = string.whitespace + string.punctuation + "\"'"


def palindrome_checker_with_deque(str1):
    d1 = Dequeue()
    d2 = collections.deque()

    for s in str1.lower():
        if s not in STRIP:
            d2.append(s)
            d1.enqueue(s)
        eq1 = True
        while d1.size() > 1 and eq1:
            if d1.dequeue_front() != d1.dequeue(): eq1 = False
        eq2 = True
        while len(d2) > 1 and eq2:
            if d2.pop() != d2.popleft(): eq2 = False
        return eq1, eq2


if __name__ == "__main__":
    str1 = "Madam Im Adam"
    print(palindrome_checker_with_deque(str1))
