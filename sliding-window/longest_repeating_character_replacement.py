class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # count = {} # hash map where keys are chars and values are char counts
        # res = 0
        # l = 0

        # # right pointer is incrementing
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     # check whether the window is valid
        #     # (right pointer - left pointer + 1) - maximum value of the chars) <= k
        #     while (r - l + 1) - max(count.values()) > k:
        #         # if not, shift the left pointer
        #         count[s[l]] -= 1
        #         l += 1
        #     # result is contantly updated
        #     res = max(res, r - l + 1)
        # return res

        ## better algorithm
        count = {} # hash map where keys are chars and values are char counts
        res = 0
        l = 0
        max_freq = 0

        # right pointer is incrementing
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                # if not, shift the left pointer
                count[s[l]] -= 1
                l += 1
            # result is contantly updated
            res = max(res, r - l + 1)
        return res
        


        """
        s = "ABAB", k = 2, res = 4
        s = "AABABBA", k = 1, res = 4
        
        """