class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_Tree():
    def __init__(self):
        self.root = None

    def insert_first(self, data):
        self.root = Node(data)

    def insert_tree(self, node, data):

        if node is None:
            node = Node(data)
            print(node.data)
        else:
            if node.data > data:
                node.left = self.insert_tree(node.left, data)

            else:
                node.right = self.insert_tree(node.right, data)

        return node

    def order_tree(self, node):
        if node is not None:
            print(node.data, end='=>')
            self.order_tree(node.left)
            self.order_tree(node.right)


if __name__ == "__main__":
    tree = Binary_Tree()
    tree.insert_first(10)
    a = int(input("몇 번 입력할 것이여?"))

    for i in range(0, a):
        data = int(input("입력할 데이터"))
        tree.insert_tree(tree.root, data)

    tree.order_tree(tree.root)

