"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    
    # our solution will be of logm + logn time complexity
    
    rows, cols = len(matrix), len(matrix[0])
    # top row and the bottom row
    top, bot = 0, rows - 1
    
    while top <= bot:
        mid_row = (top+bot) // 2
        
        # check whether the target is greater than the last number at the middle row
        if target > matrix[mid_row][-1]: 
            top = mid_row + 1
            
            
        # check whetheer the target is less than the first number   at the middle row
        elif target < matrix[mid_row][0]:
            bot = mid_row - 1
        
        else:
            break
    
    if not (top<= top):
        return False
    row = (top+bot) // 2
    l, r = 0, cols -1
    while l <= r:
        m = (l+r) //  2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


"""
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""


"""

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""