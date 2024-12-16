from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def bellman_ford(n, graph, source, target):
    # Initialize distances and parent pointers
    distance = [float('inf')] * (n + 1)
    distance[source] = 0
    parent = [None] * (n + 1)

    # Relax all edges (n - 1) times
    for _ in range(n - 1):
        updated = False
        for edge in graph:
            if distance[edge.source] == float('inf'):
                continue
            new_distance = distance[edge.source] + edge.weight
            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = edge.source
                updated = True
        if not updated:
            break

    # Check for negative weight cycles
    for edge in graph:
        if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
            return "Negative Cycle Detected"

    # Reconstruct the shortest path
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return f"{' '.join(map(str, path))}\n{distance[target]}"


# Input reading
n = int(input())
e = int(input())

graph = []
for _ in range(e):
    source, destination, weight = map(int, input().split())
    graph.append(Edge(source, destination, weight))

source = int(input())
target = int(input())

# Run Bellman-Ford algorithm
result = bellman_ford(n, graph, source, target)
print(result)
