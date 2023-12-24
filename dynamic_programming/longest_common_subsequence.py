## longest_common_subsequence

"""
Inputs: 2 strings
Output: an integer of len of the longest subsequence string


Cases:
1. General case (with strings)
2. General case (with list)
3. No common subsequence
4. One is a subsequence of the other
5. One sequence is empty
6. Both sequences are empty
7. multiple subsequences with the same length
"""

# recursive solution
"""
lcs - longest common subsequence
1. create 2 counters idx1, and idx2 starting an 0. Our solution will compute lcs of str1[idx1:] and str2[idx2:]
2. if str1[idx1:] == str2[idx2:], then the character belongs to the lcs of str1[idx1:] and str2[idx2:]; Further the length this is lcs is one more than the lcs
    of str1[idx1 + 1:] and str2[idx2 + 1:]
3. if not, then the lsc of str1[idx1:] and str2[idx2:] is the longer among lcs of str1[idx1 + 1:], str2[idx2:] and lcs of str1[idx1:], str2[idx2 + 1:]
4. if either str1[idx1:] or str2[idx2:] is empty, then their lcs is 0

"""

def lcs_recursive(str1 ,str2, idx1 = 0, idx2 = 0,):
    """
    time complexity: O(2**(n+m))
    space complexity: O(1)
    """
    if idx1 == len(str1) or idx2 == len(str2):
        return 0
    if str1[idx1] == str2[idx2]:
        return 1 + lcs_recursive(str1, str2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(str1, str2, idx1+1, idx2)
        option2 = lcs_recursive(str1, str2, idx1, idx2+1)
        return max(option1, option2)
print("-------Recursive solution------------")   
print("expected: 3", "output :", lcs_recursive("silent", "listen"))
print("expected: 7", "output :",lcs_recursive("serendipitous", "precipitation"))
print("expected: 5", "output :",lcs_recursive("dense", "condensed"))
print("expected: 5", "output :",lcs_recursive([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]))
print("======================================")



"""
Memoized solution:
1. create a dictionary to store keys as a tuple with idx1 and idx2
2. create a recurse function which computes, stores and returns computations for a given key pair
3. inside the recurse function, the first thing to do is to create a key out of the indices given
4. We then check whether the key-pair is available in the memo, if it does, we return it's value
5. check if either idx1 and idx2 are equal to len(seq1) and len(seq2) respectively.
    if either is, set memo[key] to 0
6. If it doesn't, we check whether the value at seq1[idx1] and seq2[idx2] are equal,
    if so we set memo[key] = 1 + recurse(idx1+1, idx2+1)
    if not, we calculate the max value from recurse(idx1+1, idx2) and recurse(idx1, idx2+1)
7. In lcs_memo function, we just return recurse with the indices as 0, 0
"""
def lcs_memo(seq1, seq2):
    """
    time complexity: m*n (total number of keys we can have in the memo)
    space_complexity: m*n
    """
    memo = {}
    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)

print("----------memoized solution-----------")
print("expected: 3", "output :", lcs_memo("silent", "listen"))
print("expected: 7", "output :",lcs_memo("serendipitous", "precipitation"))
print("expected: 5", "output :",lcs_memo("dense", "condensed"))
print("expected: 5", "output :",lcs_memo([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]))
print("======================================")


"""
Dynamic programming:
This uses iteration

assuming n is length of 

1. Create a matrix (table) of size (n+1) * (m+1) initialized with 0s
2. matrix[i][j] represents the lcs of seq1[:i] and seq2[:j]
    (assuming i and j are what we earlier called idx1 and idx2 respectively)
3. if seq1[i] and seq2[j] are equal, then matrix[i+1][j+1] = 1 + matrix[i][j]
4. if seq1[i] and seq2[j] are not equal, then matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])
5. return the last element (matrix[-1][-1])

     A G A C T G T C
   0 0 0 0 0 0 0 0 0
T  0 0 0 0 1 1 1 1 1
A  0 1 1 1 1 1 1 1 1
G  0 1 2 2 2 2 2 2 2
T  0 1 2 2 2 3 3 3 3
C  0 1 2 2 3 3 3 3 4
A  0 1 2 3 3 3 3 3 4
C  0 1 2 3 4 4 4 4 4
G  0 1 2 3 4 4 5 5 5

"""

def lcs_dp(seq1, seq2):
    """
    time complexity: O(n * m) // we have to iterate through all the elements in the matrix
    space complexity O(n * m) we create an array of arrays of size n * m
    )
    """
    n, m = len(seq1), len(seq2)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for idx1 in range(n):
        for idx2 in range(m):
            if seq1[idx1] == seq2[idx2]:
                matrix[idx1+1][idx2+1] = 1 +matrix[idx1][idx2]
            else:
                matrix[idx1+1][idx2+1] = max(matrix[idx1][idx2+1], matrix[idx1+1][idx2]) # go to prev column or prev row
    return matrix[-1][-1]

print("-----Dynamic programming solution-----")
print("expected: 3", "output :", lcs_dp("silent", "listen"))
print("expected: 7", "output :",lcs_dp("serendipitous", "precipitation"))
print("expected: 5", "output :",lcs_dp("dense", "condensed"))
print("expected: 5", "output :",lcs_dp([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]))
print("======================================")