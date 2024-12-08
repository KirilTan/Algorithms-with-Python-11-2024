def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node is visited:
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)

graph = {}

line = input()
while line != 'End':

    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

    line = input()

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
