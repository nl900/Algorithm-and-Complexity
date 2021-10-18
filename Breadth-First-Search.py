"""
BFS is an algorithm for traversing a tree or graph.
It starts at the root (for a tree) or an arbitrary node of a graph referred to as a search key.
It explores all neighbour nodes first before moving to the next level neighbours.

Time complexity is the total number of vertices and edges O(V+E) in the connected graph 
when it's represented as an adjacency list. As every vertix is entered into at most onceand each edge 
is checked at most twice, once for each of its vertices it's incident on.
Space complexity is O(V) as need to hold all vertices.

Below is an iterative implementation of BFS where a queue is used to do the traversal
"""


visited = [] #keep track of nodes that has been visited

def bfs(graph, visited, node):
    visited.append(node)
    queue = [] # keep track of what has been visited
    queue.append(node)
    while queue: # loop until the queue is empty
        v = queue.pop(0) #remove the first
        print(v, end=" ") #reachable node
        
        # get all neighbours of the node just removed
        for neighbour in graph[v]:
            if neighbour not in visited:
                # mark as visited and add to queue
                visited.append(neighbour)
                queue.append(neighbour)
    
#Graph in the form of an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

bfs(graph, visited, '5') 
    
