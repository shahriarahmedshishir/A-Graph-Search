def shortest_path(edges, start, goal):
    graph = {}
    for x, y, z in edges:
        graph[x] = graph.get(x, []) + [(y, z)]
        graph[y] = graph.get(y, []) + [(x, z)]  

    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    distance[start] = 0
    unvisited = set(graph)

    while unvisited:
        current = min(unvisited, key=lambda node: distance[node])
        unvisited.remove(current)
        if current == goal:
            break
        for neighbor, cost in graph[current]:
            new_dist = distance[current] + cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                parent[neighbor] = current

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, distance[goal]

def is_consistent(edges, h_value):
    for u, v, cost in edges:
        if h_value[u] > cost + h_value[v] or h_value[v] > cost + h_value[u]:
            return False
    return True


edges = [
    [0,1,2],[0,2,4],[0,3,4],[1,4,5],[1,5,3],
    [2,5,7],[3,5,3],[3,6,8],[4,7,6],[5,7,4],
    [5,9,5],[6,9,6],[7,8,2],[9,8,2]
]
heuristic_value = [10,7,6,8,5,4,3,1,0,1]

path, cost = shortest_path(edges, 0, 8)
print("Shortest Path:", path)
print("Total Cost:", cost)
if is_consistent(edges, heuristic_value):
    print("It is Consistent")
else:
    print("It is Inconsistent")