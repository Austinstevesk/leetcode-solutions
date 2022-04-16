"""
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

"""



class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            # encode the strings to one string by adding the length of the string and # before the string
            res += str(len(s)) + '#' + s
        return res
        
        
        
    def decode(self, str):
        # set i to be initially 0
        res, i = [], 0
        
        # while i is less than the length of the str
        while i < len(str):
            # we set j to be the current value of i
            j = i
            # while the char at j is not #
            while str[j] != '#':
                j += 1
            # get lenth on the string
            length = int(str[i:j])
            
            # we start at j+1 since we know the next character from # is where our string starts
            # we end at j+length+1 since we now have the total length of the string, we add 1 since we start at j+1
            res.append(str[j+1: j+length+1])
            
            # we reset i to be the start of the next word
            i = j+length+1
        
        return res
            
        
        
soln = Solution()
print(soln.encode(['my', 'dad', 'is', 'coming']))
# output - 2#my3#dad2#is6#coming
print(soln.decode('2#my3#dad2#is6#coming'))
            
