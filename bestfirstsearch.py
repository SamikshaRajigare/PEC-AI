def best_first_search(graph, start, goal, heuristic):
    visited = set()
    queue = [start]
    while queue:
        node = min(queue, key=lambda x: heuristic[x])
        queue.remove(node)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            if node == goal:
                break
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}
print("Best First Search:")
best_first_search(graph, 'A', 'F', heuristic)