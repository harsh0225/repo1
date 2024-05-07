from collections import defaultdict
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs_util(graph, v, visited):
    visited.add(v)
    print(v, end=' ')

    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs_util(graph, neighbor, visited)

def dfs(graph, v):
    visited = set()
    dfs_util(graph, v, visited)

def bfs(graph, v):
    visited = set()
    queue = [v]
    visited.add(v)

    while queue:
        v = queue.pop(0)
        print(v, end=' ')

        for neighbor in graph[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Take input from the user to construct the graph
graph = defaultdict(list)
n = int(input("Enter the number of edges: "))
print("Enter the edges (u v) one by one:")
for _ in range(n):
    u, v = map(int, input().split())
    add_edge(graph, u, v)

# Choose the starting vertex for traversals
start_vertex = int(input("Enter the starting vertex for traversals: "))

# Perform DFS and BFS traversals
print("DFS traversal starting from vertex {}: ".format(start_vertex))
dfs(graph, start_vertex)
print("\nBFS traversal starting from vertex {}: ".format(start_vertex))
bfs(graph, start_vertex)