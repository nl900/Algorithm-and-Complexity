"""
Traversal on graph or tree structures. It explores as far as possible down each branch before
backtracking.

Time complexity on average is O(V+E) or O(n+m)on a graph when represented as an adjacency list (higher if using a list), 
V=n is the number of vertices and E=m is the number of edges.
On a tree, it's O(V).
A tree is a subset of graphs has N nodes and (N-1) edges and all nodes must be reachable from the 
root and exactly one possible path from the root to the node.
Graphs have no rules its connections and may contain any set of edges that can connect nodes in any way.

Space complexity O(bm), b is the max branching factor and m is the max depth of the state space.
Needing to store b nodes for each of the m nodes.
"""

visited = set() # Set to keep track of visited nodes.

def recurs_dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            recurs_dfs(visited, graph, neighbour)
