def shortest_path(edges, heuristic, start, goal):
    graph = {}
    for x, y, z in edges:
        graph[x] = graph.get(x, []) + [(y, z)]
        graph[y] = graph.get(y, []) + [(x, z)]

    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    distance[start] = 0
    unvisited = set(graph)

    while unvisited:
        current = min(unvisited, key=lambda node: distance[node] + heuristic[node])
        
        if current == goal:
            break
        
        unvisited.remove(current)

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

edges = []
heuristic_value = []
no_of_vertices, no_of_edges = map(int, input("Enter vertices edges: ").split())

edges = []
for _ in range(no_of_edges):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))

heuristic_value = list(map(int, input("Enter heuristic values: ").split()))
goal_index = -1 

for index, value in enumerate(heuristic_value):
  if value == 0:
    goal_index = index
    break

path, cost = shortest_path(edges, heuristic_value, 0, goal_index)
print("A* Search Path:", path)
print("Total Cost:", cost)

if is_consistent(edges, heuristic_value):
    print("The heuristic is Consistent")
else:
    print("The heuristic is Inconsistent")