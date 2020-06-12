class Heapify(object):
    def __init__(self, data = None):
        self.data = data
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify(i)

    def left_child(self, i): return (2 * i) + 1

    def right_child(self, i): return (2 * i) + 2

    def __max_heapify(self, i):
        largest = i
        left = self.right_child(i)
        right = self.right_child(i)
        n = len(self.data)

        largest = ((left < n and self.data[left] > self.data[i]) and left) or i
        largest = ((right < n and self.data[right] > self.data[largest]) and right) or largest

        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            print("index {0} = {1}".format(i, self.data))
            self.__max_heapify(largest)

if __name__ == "__main__":
    list = [3, 2, 5, 1, 7, 8, 2]
    Heapify(list)