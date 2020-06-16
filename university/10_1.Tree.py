class Tree:
    def __init__(self, data, left_child=None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


root = None
level_q = []


def levelorder_traverse(tree):
    global level_q
    level_q.append(tree)
    while len(level_q) != 0:
        visit_node = level_q.pop(0)
        print("visited node = {0}".format(visit_node.data))
        if visit_node.left_child is not None: level_q.append(visit_node.left_child)
        if visit_node.right_child is not None: level_q.append(visit_node.right_child)


def init_Tree():
    global root
    leaf = []
    for i in range(6): leaf.append(Tree(i+1))
    left_subtree = Tree(9, Tree(7, leaf[0], leaf[1]), Tree(8, leaf[2], leaf[3]))
    right_subtree = Tree(10, leaf[4], leaf[5])
    root = Tree(11, left_subtree, right_subtree)


if __name__=="__main__":
    init_Tree()
    levelorder_traverse(root)
