def is_anagram(s, t):
    # to achieve space complexity of O(1), we can just use sort and sort the two strings
    #return sorted(s) == sorted(t)
    
    # space complexity = O(n), time complexity = O(n)
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) # the get method helps us set a default which is 0 if it doesn't exist in 
        countT[t[i]] = 1 + countT.get(t[i], 0)
        
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
            
    return True
    
# using collections but this is like cheating

# from collections import Counter
# def is_anagram(s, t):
#     return Counter(s) == Counter(t)
    
print(is_anagram('abcdn', 'ncbdd'))


        
        
