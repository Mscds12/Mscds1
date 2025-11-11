class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adj_list[v].append(w)

    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited)

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print("DFS Traversal:")
g.dfs(0)  # Output: 0 1 3 4 2