"""
You are in charge of selecting a football team from a large pool of players.
Each player has a cost, and a rating. You have a limited budget. What is the highest
total rating a team that fits your budget. Assume there is no minimum or maximum team size.

Given n elements, each of which has a weight and a profit, determine the maximum profit that can be
obtained by selecting a subset of elements weighing no more than w.

profit: [2,3,1,5,4,7]
weight: [4,5,1,3,2,5]
w: 15


inputs:
weights: a lis of numbers containing weights
profits: a list of numbers containing profits (same length as weights)
capacity: the maximum weight allowed

output:
max_profit: maximum profit that can be obtained by selecting elements of total weight no more than capacity
"""

"""
Test cases
1. All the elements can be included
2. None of the elements can be included
3. Only one of the elements can be included
4. You do not use the entire capacity
"""

"""
1. Write a function that computes max_profit(weights[idx:], profits[idx:], capacity) with idx starting from 0
2. If weights[idx] > capacity, the current element cannot be selected, so the maximum profit is the same as
    max_profit(weights[idx+1:], profits[idx+1:], capacity)
3. otherwise, there are 2 possibilities: we either pick weights[idx] or we don't.
    We can recursively compute the maximum
    
    i: If we don't pick it, again the max profit for this case is
        max_profit(weights[idx+1:], profits[idx+1:], capacity)
    ii: If we pick it, the maximum profit for this case is 
        profits[idx] + max_profit(weights[idx+1:], profits[idx+1:], capacity - weights[idx])
4. If weights[idx:] is empty, the maxim profit for this case is 0
"""
def max_profit_recursive(weights, profits, capacity, idx=0):
    """
    time complexity: O(2**n)
    space complexity: O(1)
    """
    if idx == len(weights) or capacity <= 0:
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(
            weights, profits, capacity, idx+1
        )
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity - weights[idx], idx+1)
        return max(option1, option2)

print("-------Recursive solution------------") 
print("expected: 19 output: ", max_profit_recursive([4,5,1,3,2,5], [2,3,1,5,4,7], 15))
print("expected: 309 output: ", max_profit_recursive([23,31,29,44,53,38,63,85,89,82], [92,57,49,68,60,43,67,84,87,72], 165))
print("expected: 0 output: ", max_profit_recursive([4,5,6], [1,2,3], 3))
print("expected: 3 output: ", max_profit_recursive([4,5,1], [1,2,3], 4))
print("expected: 1735 output: ", max_profit_recursive([41, 50, 49, 59, 55, 57, 60], [442, 525, 522, 593, 546, 564, 617], 170))
print("expected: 6 output: ", max_profit_recursive([4,5,6], [1,2,3], 15))
print("======================================")


"""
Memoized solution
"""
def max_profit_memo(weights, profits, capacity, idx=0):
    """
    time complexity: n * capacity
    space complexity: n * capacity
    """
    memo = {}
    def recurse(weights, profits, capacity, idx=0):
        key = (capacity, idx)
        if key in memo:
            return memo[key]
        else:
            if idx == len(weights) or capacity <= 0:
                return 0
            if weights[idx] > capacity:
                memo[key] = recurse(weights, profits, capacity, idx + 1)
            else:
                option1 = recurse(weights, profits, capacity, idx + 1)
                option2 = profits[idx] + recurse(weights, profits, capacity - weights[idx], idx + 1)
                memo[key] = max(option1, option2)
        return memo[key]
    return recurse(weights, profits, capacity)

print("----------memoized solution-----------")
print("expected: 19 output: ", max_profit_memo([4,5,1,3,2,5], [2,3,1,5,4,7], 15))
print("expected: 309 output: ", max_profit_memo([23,31,29,44,53,38,63,85,89,82], [92,57,49,68,60,43,67,84,87,72], 165))
print("expected: 0 output: ", max_profit_memo([4,5,6], [1,2,3], 3))
print("expected: 3 output: ", max_profit_memo([4,5,1], [1,2,3], 4))
print("expected: 1735 output: ", max_profit_memo([41, 50, 49, 59, 55, 57, 60], [442, 525, 522, 593, 546, 564, 617], 170))
print("expected: 6 output: ", max_profit_memo([4,5,6], [1,2,3], 15))
print("======================================")



"""
Dynamic programming solution
we almost always have to create a matrix for this

1. create a matrix of size (n+1) * (capacity + 1) consisting of 0s where n is the number of elements
2. matrix[i][c] represents the maximum profit that can be obtained using the first i elements of the maximum capacity is c.

Assume capacity is 10 and the weights and profits arrays are [2,3,3,4,6] and [1,2,5,9,4] respectively

explanation:
    when capacity is 0 and 1, we can't pick any elements since the least capacity we have to choose from is 2
    at capacity 2, we can pick the profit 1
    at capacity 3, we have a choice to pick profit from weight 2 or weight 3; pick the maximum -> for weight 3 (2)
    at capacity 4, we can pick from weight 2 or 3, the highest profit is on 3 (2)
    at capacity 5, we can pick from both weight 2 and 3, so we add the 2 profits (1 + 2) = 3
    and so on ... 
    
    in layman's; if we don't choose an element, the value comes from the above row
                if we choose the element and the capacity is exhausted, then the value is the profit for that weight
                if we choose the element and the capacity is not exhausted, then we have profit as curr profit
                    for matrix[i][c] + profit at matrix[i-1][c-cur_weight]

 
        0  1  2  3  4  5  6  7  8  9  10
        0  0  0  0  0  0  0  0  0  0  0
2(1)    0  0  1  1  1  1  1  1  1  1  1
3(2)    0  0  1  2  2  3  3  3  3  3  3
3(5)    0  0  1  5  5  6  7  7  8  8  8
4(9)    0  0  1  5  9  9  10 14 14 15 16
6(4)    0  0  1  5  9  9  10 14 14 15 16

3. We'll fill the matrix row by row and column by column. matrix[i][c] can be filled using some values in the row above it
4. if weights[i] > c ie thr current element is larger than capacity, then matrix[i+1][c] is simply equal to matrix[i][c]
    (since there is no way we can pick this element)
4. if weights[i] <= c, then we have 2 choices:
    i. pick the current element
    ii. not picking the current element to get value of matrix[i+1][c].
    
    we can compare the maximum profit for both these options and pick the better one as value of matrix[i][c]
    
"""

def max_profit_dp(weights, profits, capacity):
    """
    time complexity: O(n * capacity) (n being the len of weights)
    space complexity: O(n * capacity)
    """
    n = len(weights)
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                matrix[i+1][c] = matrix[i][c]
            else:
                # max of whether we choose it or not
                matrix[i+1][c] = max(
                    matrix[i][c],
                    profits[i] + matrix[i][c-weights[i]]
                )
    return matrix[-1][-1]

print("-----Dynamic programming solution-----")
print("expected: 19 output: ", max_profit_dp([4,5,1,3,2,5], [2,3,1,5,4,7], 15))
print("expected: 309 output: ", max_profit_dp([23,31,29,44,53,38,63,85,89,82], [92,57,49,68,60,43,67,84,87,72], 165))
print("expected: 0 output: ", max_profit_dp([4,5,6], [1,2,3], 3))
print("expected: 3 output: ", max_profit_dp([4,5,1], [1,2,3], 4))
print("expected: 1735 output: ", max_profit_dp([41, 50, 49, 59, 55, 57, 60], [442, 525, 522, 593, 546, 564, 617], 170))
print("expected: 6 output: ", max_profit_dp([4,5,6], [1,2,3], 15))
print("======================================")