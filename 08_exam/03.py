class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def roads_builder():
    # Input parsing
    e = int(input())
    edges = []
    city_to_index = {}
    city_counter = 0

    critical_edges = []
    all_edges = []

    for _ in range(e):
        line = input().split()
        city1, city2, distance = line[:3]
        distance = int(distance)
        is_critical = len(line) == 4 and line[3] == "critical"

        # Map cities to indices for Union-Find
        if city1 not in city_to_index:
            city_to_index[city1] = city_counter
            city_counter += 1
        if city2 not in city_to_index:
            city_to_index[city2] = city_counter
            city_counter += 1

        idx1, idx2 = city_to_index[city1], city_to_index[city2]
        edge = (distance, idx1, idx2, is_critical)

        all_edges.append(edge)
        if is_critical:
            critical_edges.append(edge)

    # Sort edges by distance
    all_edges.sort(key=lambda x: x[0])

    # Initialize Union-Find
    uf = UnionFind(city_counter)

    # Include all critical edges first
    total_distance = 0
    for distance, city1, city2, _ in critical_edges:
        if uf.find(city1) != uf.find(city2):
            uf.union(city1, city2)
            total_distance += distance

    # Add non-critical edges to complete the MST
    for distance, city1, city2, is_critical in all_edges:
        if not is_critical and uf.find(city1) != uf.find(city2):
            uf.union(city1, city2)
            total_distance += distance

    print(total_distance)


roads_builder()
