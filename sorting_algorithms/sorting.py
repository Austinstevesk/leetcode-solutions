"""
sorting algorithms

Cases:
some list of numbers in random order
an already sorted list
a list that is sorted in descending order
a list that contains repeating elements
an empty list
a list with just one element
a list with only one element repeating several times
a really long list


"""

def bubble_sort(nums):
    """
    time complexity O(n**2)
    space complexity O(1)
    """
    for _ in range(len(nums) -1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

print("-----------Bubble sort-------------")
print(bubble_sort([4,2,6,7,3,1,4,5,2]))
print(bubble_sort([3,4,5,6,7,8,9,10,20]))
print(bubble_sort([20,10,9,8,7,6,5,4,3]))
print(bubble_sort([-5,-12,2,6,1,23,7,7,-12,6,1]))
print(bubble_sort([]))
print(bubble_sort([6]))
print(bubble_sort([2,2,2,2,2,2,2,2,2]))
print("=====================================")


def insertion_sort(nums):
    """
    time complexity O(n**2)
    space complexity O(1)
    """
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i -1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums
print("-----------Insertion sort-------------")
print(insertion_sort([4,2,6,7,3,1,4,5,2]))
print(insertion_sort([3,4,5,6,7,8,9,10,20]))
print(insertion_sort([20,10,9,8,7,6,5,4,3]))
print(insertion_sort([-5,-12,2,6,1,23,7,7,-12,6,1]))
print(insertion_sort([]))
print(insertion_sort([6]))
print(insertion_sort([2,2,2,2,2,2,2,2,2]))
print("=====================================")


# Divide and conquer
"""
1. Divide the input into roughly two equal parts
2. Recursively solve the problem individually for each of the two parts
3. Combine the results to solve the problem for the original inputs
4. include terminating conditions for the small or indivisible inputs
"""

"""
- if the input is empty or contains just one element. it is already sorted. return it
- if not, divide the list of numbers into roughly two equal parts
- sort each part recursively using the merge sort algorithm. You'll get back 2 sorted lists
- merge the two sorted lists to get a single sorted list
"""

def merge(list1, list2, depth=0):
    print(" "*depth, "merge:", list1, list2)
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    list1_tail = list1[i:]
    list2_tail = list2[j:]
    return merged + list1_tail + list2_tail


def merge_sort(nums, depth=0):
    """
    time complexity O(nlogn) = merge * height of tree = n * log n
    space complexity O(n)
    """
    print(" "*depth, "merge_sort:", nums)
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    left_sorted, right_sorted = merge_sort(left, depth+1), merge_sort(right, depth+1)
    sorted_nums = merge(left_sorted, right_sorted, depth+1)
    return sorted_nums

print("---------------Merge sort-------------")
# print(merge_sort([4,2,6,7,3,1,4,5,2]))
# print(merge_sort([3,4,5,6,7,8,9,10,20]))
# print(merge_sort([20,10,9,8,7,6,5,4,3]))
print(merge_sort([-5,-12,2,6,1,23,7,7,-12,6,1]))
# print(merge_sort([]))
# print(merge_sort([6]))
# print(merge_sort([2,2,2,2,2,2,2,2,2]))

# import random
# in_list = list(range(10000))
# out_list = list(range(10000))
# random.shuffle(in_list)
# print(merge_sort(in_list))
print("=====================================")



"""
- if the list is empty or contains one element, return it. It is already sorted
if not:
- pick a random element from the list, this is called pivot
- re-order the list so that all elements wu=ith values less than or equal to pivot come before the pivot,
while all elements with values greater than the pivot come after it. (This operation is called partitioning)
- the pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort
"""

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end - 1
    while l < r:
        # increment the left pointer if number is less than or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        
        # decrement the right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        # two out of place elements found so we swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

def quick_sort(nums, start=0, end=None):
    """
    average time complexity O(nlogn) = partition * height of tree = n * log n
    worst time complexity O(n**2) when the pivot chosen is the smallest element that creating a skewed tree
        whose height is no longer logn but n
    space complexity O(1)
    """
    if end is None:
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    return nums 


print("-----------Quick sort-------------")
print(quick_sort([4,2,6,7,3,1,4,5,2]))
print(quick_sort([3,4,5,6,7,8,9,10,20]))
print(quick_sort([20,10,9,8,7,6,5,4,3]))
print(quick_sort([-5,-12,2,6,1,23,7,7,-12,6,1]))
print(quick_sort([]))
print(quick_sort([6]))
print(quick_sort([2,2,2,2,2,2,2,2,2]))
print("=====================================")



"""
Problem statement

You are working on a feature 'Top Notebooks' of the week.
Write a function to sort a list of notebooks in decreasing order of likes.
Keep in mind that upto millions of notebooks can be created every week so your function
needs to be as efficient as possible

"""

class Notebooks:
    def __init__(self, title, username, likes) -> None:
        self.title, self.username, self.likes = title, username, likes
    
    def __repr__(self) -> str:
        return 'Notebook <"{}/{}", {} likes'.format(self.username, self.likes, self.likes)
    