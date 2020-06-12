def bfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            print(current)
            for i in graph[current]:
                queue.append(i)


def dfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        current = queue.pop(-1)
        if current not in visited:
            visited.append(current)
            print(current)
            for i in graph[current]:
                queue.append(i)


if __name__ == "__main__":

    graph = [
        [1, 2],
        [0, 3],
        [0, 4, 5],
        [1],
        [2, 6],
        [2],
        [4]
    ]

    dfs(graph, 0)