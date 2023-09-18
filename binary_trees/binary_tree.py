class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)

# left, root, right 
def print_in_order(r):
    if r is None:
        return
    print_in_order(r.left)
    print(r.data, end=" ")
    print_in_order(r.right)

# root, left, right
def print_pre_order(r):
    if r is None:
        return
    print(r.data, end=" ")
    print_pre_order(r.left)
    print_pre_order(r.right)

# root, right, left
def print_post_order(r):
    if r is None:
        return
    print(r.data, end=" ")
    print_post_order(r.right)
    print_post_order(r.left)


node = Node("g")
node.insert("c")
node.insert("b")
node.insert("a")
node.insert("e")
node.insert("d")
node.insert("f")
node.insert("i")
node.insert("h")
node.insert("j")
node.insert("k")

print_in_order(node)
print(" -> in-order traversal")
print_pre_order(node)
print(" -> pre-order traversal")
print_post_order(node)
print(" -> post-order traversal")



## adjacency list -> list of nodes indicating what the children of the nodes are
# we'll use a dict > key is value of the nodes, value is the list of children

d = {}
def make_adjacency_list(r):
    if r is None:
        return
    d[r.data] = []
    make_adjacency_list(r.left)
    if r.left:
        d[r.data].append(r.left.data)
    if r.right:
        d[r.data].append(r.right.data)
    make_adjacency_list(r.right)
    return d

print()
print("adjacency list")
a_list = make_adjacency_list(node)
for ele in a_list:
    print(f"{ele}:{d[ele]}")
    
## breadth-first-search
# navigates through the binary tree in levels from the top
# uses a queue

import collections
def bfs(adjacency_list):
    queue = collections.deque("g")
    visited = []
    
    while queue:
        node = queue.popleft()
        visited.append(node)
        # [queue.append(x) for x in adjacency_list[node]]
        for x in adjacency_list[node]:
            queue.append(x)
    return visited

print()
print("breadth first search")
print(bfs(a_list))


# depth-first-search
# uses stack

def dfs(adjacency_list):
    stack = ["g"]
    visited = []
    
    # while len(stack) > 0:
    while stack:
        node = stack.pop()
        visited.append(node)
        # for x in node:
        #     visited.append(adjacency_list[x])
        [stack.append(x) for x in adjacency_list[node]]
    # can be from left or from right
    # from right ['g', 'i', 'j', 'k', 'h', 'c', 'e', 'f', 'd', 'b', 'a'] -> this is actually post-order traversal
    # from left ["g", "c", "b", "a", "e", "d", "f", "i", "h", "j", "k"] -> pre-order traversal
    return visited

print()
print("depth first search")
print(dfs(a_list))



# search for a key for a tree
# can use bfs or dfs
def search(al, key):
    stack = ["g"]
    visited = []
    found = False
    
    while stack:
        node = stack.pop()
        if node == key:
            return True
        else:
            if node not in visited:
                visited.append(node)
                [stack.append(x) for x in al[node]]
    return found

print()
print("search in binary tree")
print(search(a_list, "a"))
print(search(a_list, "y"))