class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## brute-force -> time limit exceeded > time complexity is O(n2)
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        
        
        
        # O(n) time complexity 
        res = 0
        l, r = 0, len(height) - 1
        for i in range(len(height)):
            while l < r:
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)
                if height[l] < height[r]:
                    l += 1

                # since the below 2 cases are doing the same thig, we can just use an else automatically
                # elif height[l] > height[r]:
                #     r -= 1
                # # if equal, just either increment l pointer or decrement r pointer
                # else:
                #     r -= 1
                else:
                    r -= 1
        return res
    
"""
[1,8,6,2,5,4,8,3,7] > 49
[1,1] > 1

"""