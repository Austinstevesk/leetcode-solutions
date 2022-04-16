"""
128. Longest Consecutive Sequence
Medium

9029

398

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""



def longest_consequtive_sequence(nums):
    num_set = set(nums)
    longest = 0
    
    for num in nums:
        # check i it is the start of the numset eg [1,2,3,4, .. 100 ...200], 1, 200,200 is the start since there is no number before them
        if (num-1) not in num_set:
            # we try to get the lenth of the sequence, we initialize length to 0
            length = 0
            while (num+length) in num_set:
                length += 1
                
                # get the longest by comparing the max of current longest and the length
                longest = max(longest, length)
    
    return longest
    
print(longest_consequtive_sequence([1,4,100,3,2,200]))
