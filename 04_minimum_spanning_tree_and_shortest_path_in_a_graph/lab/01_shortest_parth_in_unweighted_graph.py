from collections import deque

nodes = int(input())
edges = int(input())

graph = []

[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
q = deque([start_node])

while q:
    node = q.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        q.append(child)
        parent[child] = node

path = deque()
node = destination_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print('Shortest path length is:', len(path) - 1)
print(*path, sep=' ')
