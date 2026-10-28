def a_star(graph, start, goal, h):
    open_list = [start]
    closed_list = []
    cost = {start: 0}

    while open_list:
        current = min(open_list,
                      key=lambda x: cost[x] + h[x])

        if current == goal:
            print(current, end=' ')
            return

        open_list.remove(current)
        closed_list.append(current)
        print(current, end=' ')

        for neighbor, c in graph[current]:
            new_cost = cost[current] + c

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}
print("A* Search:")
a_star(graph, 'A', 'G', h)