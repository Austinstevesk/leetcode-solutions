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
edges = [(0,1), (0,4), (1,2), (2,3), (1,3), (1,4), (3,4)]
graph1 = Graph(num_nodes, edges)

# print(graph1)

def dfs(graph: Graph, source):
    """
    time complexity: n+m (n + 2m assuming m are the total number of edges)
    space complexity: n+m
    """
    stack = []
    discovered = [False] * len(graph.data)
    visited = []
    parent = [None] * len(graph.data)
    
    stack.append(source)
    
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            visited.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    parent[node] = current
                    stack.append(node)
    return visited, parent

print(dfs(graph1, 3))


def detect_cycle_in_graph(graph: Graph, source):
    visited = []
    discovered = [False] * len(graph.data)
    stack = [source]
    has_cycle = False
    no_of_cycles = 0
    
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            visited.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
        else:
            has_cycle = True
            no_of_cycles += 1
    return has_cycle, no_of_cycles

print(detect_cycle_in_graph(graph1, 3))

graph2 = Graph(num_nodes=5, edges=[(0,1), (0,3), (0,2), (1,2), (3,4)])
print(dfs(graph2, 3))
print(detect_cycle_in_graph(graph2, 3))