from typing import List

"""
"""

class Graph:
    def __init__(self, num_nodes: int, edges: List[tuple]) -> None:
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            # insert into the right lists
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(n, neighbours) for n, neighbours in enumerate(self.data)])
    
    # This helps to stringify the object without the need of using print(instantiated object)
    def __str__(self) -> str:
        return self.__repr__()
    
def add_edge_to_graph(graph: Graph, edge: tuple):
    idx, value = edge
    if idx <= len(graph.data):
        graph[idx].append(value)
    else:
        graph.append([value])
    
num_nodes = 5
edges = [(0,1), (0,4), (1,2), (2,3), (1,3), (1,4), (3,4)
]
graph1 = Graph(num_nodes, edges)

# print(graph1)


def bfs(graph: Graph, source):
    
    queue = []
    discovered = [False] * len(graph.data)
    distance = [0] * len(graph.data)
    parent = [None] * len(graph.data)
    
    discovered[source] = True
    distance[source] = 0
    queue.append(source)
    
    idx = 0
    
    while idx < len(queue):
        
        # simulate deque
        current = queue[idx]
        idx += 1
        
        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return {
        "queue": queue,
        "distance": distance,
        "parent": parent
    }

# print(bfs(graph1, 3))


# check if all nodes are connected
# len of queue should be equal to total number of queue
import collections
def check_all_nodes_connected_nodes(graph: Graph, source):
    queue = collections.deque([source])
    visited = [source]
    distance = [0] * len(graph.data)
    count = 0
    
    while queue:
        current = queue.popleft()
        count += 1
        for node in graph.data[current]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
                distance[node] = 1 + distance[current]
    return len(graph.data) == count

print(check_all_nodes_connected_nodes(graph1, 2))


## find the number of connected components


graph2 = Graph(num_nodes=9, edges=[(0,1), (0,3), (1,2), (2,3), (4,5), (4,6), (5,6), (7,8)])
"""
[(0,1), (0,3), (1,2), (2,3), // connected components
(4,5), (4,6), (5,6), // connected components
(7,8) // connected components
]
"""
print(bfs(graph2, 0))
print(check_all_nodes_connected_nodes(graph2, 0))
def find_number_of_connected_components():
    ...