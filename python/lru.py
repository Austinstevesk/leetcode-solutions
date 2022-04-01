"""
In order to implement an LRU cache we need a doubly linked list.
This will help us to maintain an ordering of the items, and know which
was least recently used, pointed to by the head pointer, and the most recently used,
pointed to by the tail pointer.
"""
class Node:
    """ Definition of the node for a doubly linked list
    """
    def __init__(self, key, val):
        """
        We store both the key and value so that we can use the key to reinsert the node into the linked list,
        after it has been accessed and been made the MRU(most recently used)
        """
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the cache as a dictionary, store the key and value and the capacity
        Set the head pointer and tail pointer to point at each other(alternatively they can point to None
        """
        self.cap = capacity
        self.cache = dict()

        # left = LRU, right = MRU
        self.tail, self.head = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        """
        Helper function that removes a node from the linked list.
        """
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """
        Helper function that inserts the node into the rightmost position
        """
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove the LRU from the list and delete from hashmap
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    print(lru.cache)
    lru.put(2, 2)
    print(lru.cache)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.cache)
    print(lru.get(2))
    lru.put(4,4)
    print(lru.cache)
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(3))
