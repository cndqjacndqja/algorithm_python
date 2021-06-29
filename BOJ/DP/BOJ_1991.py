class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def pre_order(node):
    print(node.item, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])


def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        in_order(tree[node.right])


def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.item, end='')


if __name__ == "__main__":
    n = int(input())
    tree = {}

    for _ in range(n):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])