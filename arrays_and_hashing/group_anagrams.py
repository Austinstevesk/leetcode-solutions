
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            print(x)
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        print(result)
        return list(result.values())



# another solution
from collections import defaultdict

def group_anagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26 # from a....z
        for c in s:
            count[ord(c) - ord("a")] += 1
            
        res[tuple(count)].append(s) # lists can never be keys so we convert this to tuple
            
    return res.values()
    
    
print(group_anagrams(['ann', 'nan', 'jack', 'man', 'job', 'dull', 'ludl']))
            
