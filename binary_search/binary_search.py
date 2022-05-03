
def search(nums, target):
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) //2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))



"""
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


"""