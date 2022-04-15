"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def product_except_self(nums):
    # we set result to have all 1's at first
    res = [1] * len(nums)
    
    # initialize prefix to 1
    
    prefix = 1
    # loop through the array from the left side
    for i in range(len(nums)):
        # set the res at index i to be the prefix
        res[i] = prefix
        # update the prefix by multiplying it with the current value at i
        prefix *= nums[i]
        
    # initialize postfix to 1
    postfix = 1
    # loop through form the right side
    for i in range(len(nums)-1, -1, -1):
        # update the current res by multiplying it with the postfix
        res[i] *= postfix
        # update the postfix by multiplying it with the current value at i
        postfix*= nums[i]
        
    return res
    
print(product_except_self([1,2,3,4]))
#res = [24,12,8,6]
