"""

Steps:
1. State the problem clearly, identify input and output formats
2. Come up with some example inputs and outputs, try to cover all edge cases
3. Come up with a correct solution foe the problem. State it in plain English
4. Implement the solution and test it using example inputs; fix bugs if any
5. Analyze complexity and identify inefficiencies if any
6. Apply the right technique to overcome the inefficiency; repeat step 3 to 6


input -> rotated list
output -> sorted list
problem -> try to determine the number of times the sorted list was rotated to make the rotated list

rotated_list = [7,9,3,5,6]
returns -> rotations (int) -> min number of times the sorted list was rotated

solution -> O(logN)

Test cases:
1. Empty list
2. A list with only one element
3. A list of size 10 that was rotated 3 times
4. A list if size 8 that was rotated 5 times
5. A list that was rotated just once
6. A list that wasn't rotated at all
7. A list that was rotated n-1 times
8. a list that was rotated n times. Do you get the original list?

"""
    
# OlogN
def linear_count_rotations(nums):
    position = 0
    while position < len(nums) - 1:
        if nums[position + 1] < nums[position]:
            return position + 1
        position += 1
    return 0

print(linear_count_rotations([]))
print(linear_count_rotations([2]))
print(linear_count_rotations([8,9,10,1,2,3,4,5,6,7]))
print(linear_count_rotations([4,5,6,7,8,1,2,3]))
print(linear_count_rotations([8,1,2,3,4,5,6,7]))
print(linear_count_rotations([1,2,3,4,5,6,7,8]))
print(linear_count_rotations([2,3,4,5,6,7,8,1]))
print(linear_count_rotations([1,2,3,4,5,6,7,8]))
print(linear_count_rotations([5,6,7,1,2,3,4]))

"""
we can use binary search here
check the middle element and the last element in the array
if the middle element is smaller than the last element, the answer lies on the left
if the middle element is larger than the last element, the answer lies on the right
"""
# logN
def count_rotations(nums):
    l, r = 0, len(nums) - 1
    if r <= 0 or nums[l] == nums[r]:
        return 0
    
    while l <= r:
        mid = (l + r) // 2
        # print("l ", l, "r ", r, "mid ", mid)
        mid_number = nums[mid]
        if mid_number < nums[mid - 1]:
            return mid
        elif mid_number < nums[-1]:
            r = mid - 1
        else:
            l = mid + 1
        
    return 0
print("Binary search")
print(count_rotations([]))
print(count_rotations([2]))
print(count_rotations([8,9,10,1,2,3,4,5,6,7]))
print(count_rotations([4,5,6,7,8,1,2,3]))
print(count_rotations([8,1,2,3,4,5,6,7]))
print(count_rotations([1,2,3,4,5,6,7,8]))
print(count_rotations([2,3,4,5,6,7,8,1]))
print(count_rotations([1,2,3,4,5,6,7,8]))
print(count_rotations([5,6,7,1,2,3,4]))

# handle repeating numbers
print(count_rotations([8,8,8,9,9,9,10,0,0,1,2,3,3,4,5,6,6,7,7]))