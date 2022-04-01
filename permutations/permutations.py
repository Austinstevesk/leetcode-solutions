def permutations(nums, n):
    unique_nums = set()
    for i in nums:
        unique_nums.add(i)
    if max(unique_nums) != n:
        return False
    if min(unique_nums) != 1:
        return False
    if len(unique_nums) != n:
        return False
    return True
    
print(permutations([-1,2,4,5,3,6], 6))