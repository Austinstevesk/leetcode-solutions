class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                # we found our lowest point, we want our pointer to be at the minimum
                l = r
            # we keep on incrementing the right pointer
            r += 1
                
        return res