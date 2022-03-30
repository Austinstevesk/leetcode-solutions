"""
DEFINITION
A heap is a data structure that ensures a key at every position is
greater than or equal to two other keys within the same data structure.
If viewed as a binary tree, a heap ensures that the key at a node is 
greater than or equal to the two children of this node if they exist.
In turn those two child keys must be greater than or equal to two other
keys and so on and so forth.

REPRESENTATION
1) As a linked list -> requires 3 links, a link to left and right child and the parent
2) Array representation -> the root comes in the first index with its left and right child at
   position 2 and 3, and their children at position 4,5,6 and 7 and so forth

parent of element at k is found at position k/2, conversely the children of a node
at k are found at 2k and 2k + 1
"""

class Heap:
    def __init__(self):
        self.heap = [None]

    def _less(self, i, j):
        return self.heap[i] < self.heap[j]

    def _exchange(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def bottom_up_reheapify(self, k):
        while k > 1 and self._less(k//2, k):
            self._exchange(k//2, k)
            k = k//2

    def top_down_reheapify(self, k):
        bottom_key = len(self.heap) - 1
        child = 2*k
        
        while child <= bottom_key:
            if child < bottom_key and self._less(child, child + 1):
                child += 1

            if (not self._less(k, child)): break

            # otherwise it's smaller than the other child
            self._exchange(k, child)
            k = child

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, val):
        last = self.size()
        self.heap.insert(last+1, val)
        self.bottom_up_reheapify(last)

    def del_max(self):
        max = self.heap[1]
        self._exchange(1, self.size()-1)
        self.heap.remove(max)
        self.top_down_reheapify(1)

        return max
