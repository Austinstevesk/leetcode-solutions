class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False) -> None:
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        for edge in edges:
            if self.weighted:
                # include weights
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # without weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
                    
    def __repr__(self) -> str:
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result
    

print("Unweighted, undirected graph")
graph1 = Graph(num_nodes=5, edges=[(0,1), (0,4), (1,2), (2,3), (1,3), (1,4), (3,4)])
print(graph1)
print("---------------------------")


print("Weighted graph")
graph2 = Graph(
    num_nodes=9,
    edges=[(0,1,3), (0,3,2), (0,8,4), (1,7,4), (2,7,2), (2,3,6), (2,5,1), (3,4,1), (4,8,8), (5,6,8)],
    weighted=True,
    )
print(graph2)
print("---------------------------")

print("Unweighted, directed graph")
graph3 = Graph(num_nodes=5, edges=[(0,1), (0,4), (1,2), (2,3), (1,3), (1,4), (3,4)], directed=True)
print(graph3)
print("---------------------------")


## shortest path in terms of total weight/cost
"""
1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity
    for all other nodes. Set the initial node as current.
3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through
    the current node.
    Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
    For example:
        if the current node A is marked with a distance of 6, and the edge connecting it with the neighbor B has length
        2, then the distance through B will be 6 + 2 = 8. If B was previously  marked with a distance greater than 8,
        then change it to 8. Otherwise, the current value will be kept
4. When we are done considering all of the unvisited neighbors of a current node, mark the current node as visited
    and remove it from the unvisited set. A visited node will never be checked again.
5. If the destination node has been marked visited (when planning a route between 2 specific nodes) or if the smallest
    tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs
    when there is no connection between the initial node and the remaining unvisited nodes), then stop. The algorithm
    has finished.
6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current
    node", and go back to step 3.
"""

def update_distances(graph, current, distance, parent=None):
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next unvisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

import collections
def shortest_path(graph: Graph, source, target):
    """
    time complexity: n**2+m (n**2 +n + 2m assuming m are the total number of edges)
    space complexity: n+m
    """
    visited =[False] * len(graph.data)
    parent =[None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    
    distance[source] = 0
    queue = collections.deque([source])
    
    while queue and not visited[target]:
        current = queue.popleft()
        # set current as visited
        visited[current] = True
        
        # update distances of all neighbors
        update_distances(graph=graph, current=current, distance=distance, parent=parent)
        
        # find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance=distance, visited=visited)
        if next_node:
            queue.append(next_node)
        
    return (
        {
            "shortest_distance": distance[target],
            "parent": parent,
        })

graph = Graph(
    num_nodes=6,
    edges=[(0,1,4), (0,2,2), (1,2,5), (1,3,10), (2,4,3), (4,3,4), (3,5,11)],
    weighted=True,
    directed=True,
    )
print("----------Weighted and directed graph-----------")
print(graph)
print("================================================")

print("-----------Get shorted path on weighted and directed graph-----------")
print("expected: 20, output: ", shortest_path(graph=graph, source=0, target=5))
print("=====================================================================")
