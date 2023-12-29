"""
You are given 2 strings, "intention" and "execution".
Find the minimum number of operations needed to convert intention to execution
The three operations are:
1. Delete (maybe delete the first i in intention)
2. Insertion (maybe insert e before intention)
3. Swap/Replace (swap the first i in intention with e)
"""


"""
Cases:
1. general case (listed above)
2. no changes required
3. all characters need to be changed
4. Both strings are of equal length
5. Both strings are of unequal length
6. one of the strings is empty
7. only deletion, only insertion, only swap
8. Both strings are empty
"""

def recurse_min_steps(str1, str2, i1=0, i2=0):
    """
    time complexity: 3*(n+m)
    space complexity: (n+m)**3
    """
    # edge cases handled first
    if i1 == len(str1):
        return len(str2) - i2
    if i2 == len(str2):
        return len(str1) - i1
    if str1[i1] ==str2[i2]:
        return recurse_min_steps(str1, str2, i1+1, i2+1)
    return 1 + min(
        recurse_min_steps(str1, str2, i1, i2+1), # insert at the beginning of str1
        recurse_min_steps(str1, str2, i1+1, i2+1), # swap character in str 1
        recurse_min_steps(str1, str2, i1+1, i2) # delete character in str1
    )


print("---------------Recursive solution----------------")
print("Expected: 5 Output: ", recurse_min_steps("intention", "execution"))
print("Expected: 0 Output: ", recurse_min_steps("execution", "execution"))
print("Expected: 2 Output: ", recurse_min_steps("good", "door"))
print("Expected: 1 Output: ", recurse_min_steps("dead", "dread"))
print("Expected: 9 Output: ", recurse_min_steps("intention", ""))
print("Expected: 1 Output: ", recurse_min_steps("ececution", "execution"))
print("Expected: 2 Output: ", recurse_min_steps("executional", "execution"))
print("Expected: 1 Output: ", recurse_min_steps("executio", "execution"))
print("Expected: 0 Output: ", recurse_min_steps("", ""))
print("=================================================")


def memo_min_steps(str1, str2,):
    """
    time complexity: m*n
    space complexity: m*n
    """
    memo = {}
    def recurse(i1, i2):
        key = (i1, i2)
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(
                recurse(i1+1, i2),
                recurse(i1, i2+1),
                recurse(i1+1, i2+1)
            )
        return memo[key]

    return recurse(0, 0) 

print("---------------Memoized solution----------------")
print("Expected: 5 Output: ", memo_min_steps("intention", "execution"))
print("Expected: 0 Output: ", memo_min_steps("execution", "execution"))
print("Expected: 2 Output: ", memo_min_steps("good", "door"))
print("Expected: 1 Output: ", memo_min_steps("dead", "dread"))
print("Expected: 9 Output: ", memo_min_steps("intention", ""))
print("Expected: 1 Output: ", memo_min_steps("ececution", "execution"))
print("Expected: 2 Output: ", memo_min_steps("executional", "execution"))
print("Expected: 1 Output: ", memo_min_steps("executio", "execution"))
print("Expected: 0 Output: ", memo_min_steps("", ""))
print("=================================================")