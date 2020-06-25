import sys


class CList:

    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_item(self): return self.size

    def is_empty(self): return self.size == 0

    def insert(self, item):
        n = self._Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def fisrst(self):
        if self.is_empty():
            print('UnderFlow')
            sys.exit(10)
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            print('UnderFlow')
            sys.exit(10)
        x = self.last.next
        if self.size == 1: self.last = None
        else: self.last.next = x.next
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty(): print("리스트 비었음.")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, '->', end = ' ')
                p = p.next
            print(p.item)


if __name__ == "__main__":
    CL = CList()
    CL.insert('A')
    CL.insert('B')
    CL.insert('C')
    CL.insert('D')

    CL.print_list()
    CL.delete()
    CL.print_list()