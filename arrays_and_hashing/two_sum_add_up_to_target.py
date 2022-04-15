class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # This solution has a time complexity of O(n) - Since wea re only iterating through the array once
        # Space complexity O(n) - We need space for the hash map
        """we get the diff which is target - n which is a number we are looping through the array,
           if the difference exists in the hash map, we return its index and the index of n, if not we update the 
           hash map using the n mapped to its index
        """
        
        prev_hash_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_hash_map:
                return [prev_hash_map[diff], i]
            prev_hash_map[n] = i
