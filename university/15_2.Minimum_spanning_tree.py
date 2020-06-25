parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    print(root1, root2)
    if rank[root1] > rank[root2]: parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    MST = list()
    for node in graph['vertices']: make_set(node)
    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            MST.append(edge)
        print(MST)
    return MST

if __name__ =="__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'edges': [(7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), (9, 'B', 'D')
                  ,(7, 'B', 'E'), (5, 'C', 'E'), (7, 'D', 'E'), (6, 'D', 'F'),
                    (8, 'E', 'F'), (9, 'E', 'G'), (11, 'G', 'F')]
    }
    MST = kruskal(graph)
    print(MST)