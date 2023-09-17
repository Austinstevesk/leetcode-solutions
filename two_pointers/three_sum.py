class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # we don't want to reuse the same value twice
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
    
    
"""
test > output
[-1,0,1,2,-1,-4] > [[-1,-1,2],[-1,0,1]]
[0,1,1] > []
[0,0,0] > [0,0,0]

"""