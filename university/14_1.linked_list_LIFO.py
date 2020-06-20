class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

    def getData(self): return self.value

    def getNext(self): return self.pointer

    def setData(self, newdata): self.value = newdata

    def setNext(self, newpointer): self.pointer = newpointer


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def _printList(self):
        print('head = {}, length = {}'.format(self.head, self.length))
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
    def _delete(self, prev, node):
        self.length -= 1
        if not prev: self.head = node.pointer
        else: prev.pointer = node.pointer

    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value: found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i: self._delete(prev, node)

    def delteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found: self._delete(prev, node)
        else: print("값 {0}에 해당하는 노드 없음.".format(value))

if __name__=="__main__":
    ll = LinkedListLIFO()

    for i in range(1, 5): ll._add(i)
    ll._printList()
    ll.deleteNode(2)
    ll._printList()
    ll._add(5)
    ll._printList()

    ll.delteNodeByValue(3)
    ll._printList()
    ll.delteNodeByValue(3)
    ll._printList()
