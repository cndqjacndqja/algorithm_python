parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]: parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    MST = list()
    for node in graph['vertices']:
        make_set(node)

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
    graph = {      'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': [(1, 'A', 'B'), (6, 'A', 'C'), (4, 'B', 'D'), (2, 'B', 'F')
                  ,(3, 'B', 'C'), (2, 'C', 'D'), (4, 'C', 'E'), (7, 'C', 'F'),(3, 'D', 'E'),
                    (1, 'D', 'F'), (5, 'E', 'F')]
    }
    MST = kruskal(graph)
    print(rank, parent)
    print(MST)
