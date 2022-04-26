import heapq
# we are using a heap since you are told to implement it in place, we should not use extra memory
# heaps help us ensure we can add elements in O(logn) as compared to arrays which are O(n) time complexity
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # create min heap with K-largest integers
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # create a heap
        while len(self.minHeap) > self.k:
            # pop the smallest since we only need to store k values which are the largest
            heapq.heappop(self.minHeap)
            

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
