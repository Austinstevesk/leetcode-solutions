"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import heapq
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res= []
    freq = {}
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)
    print(freq)
        
    for key, value in freq.items():
        if len(res) < k:
            heapq.heappush(res, [value, key])
        else:
            heapq.heappushpop(res, [value, key])
            
    return [key for value, key in res]

print(topKFrequent([1,1,1,2,4,3,2], 2))


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = []
        for i in nums:
            count[i] = 1+ count.get(i, 0)
        count = sorted(count.items(), key = lambda x: x[1], reverse=True)

        for i in range(k):
            freq.append(count[i][0])
            
        return freq
            
