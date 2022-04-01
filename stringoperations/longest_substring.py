class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 # the left index
        res = 0 # the right index
        char_set = set() # we create a set since it can never store duplicates, - You can choose to use list for this case
        
        for right in range(len(s)):

            # use while loop since it checks repeatitively
            while s[right] in char_set:
                # you need to remove the recurring letter on the left pointer
                char_set.remove(s[left])
                left += 1
                
            char_set.add(s[right])
            
            """
            res is at first 0, then doing the maths; max(res, (right+1 - left)) using eg "abcabcab", we have 3 as the new
            res since we have 3 as the longest substring without repetition.

            the function max continues till we loop through the entire string.

            We need to add 1 since we are using indices. For example, the left at first is 0, then the right is at 2 where we
            have the first c. [2-0] = 2, but the number of letters is 3 so we add 1
            """
            res = max(res, (right + 1 - left))
            
        return res