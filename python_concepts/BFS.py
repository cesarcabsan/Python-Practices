graph = {"A": ["B", "G", "D"],
         "B": ["A", "F", "E"],
         "C": ["F", "H"],
         "D": ["F", "A"],
         "E": ["B", "G"],
         "F": ["B", "D", "C"],
         "G": ["A", "E"],
         "H": ["C"]
}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop()
        print(s, '', end='')

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

bfs(visited, graph, "D")
     


 