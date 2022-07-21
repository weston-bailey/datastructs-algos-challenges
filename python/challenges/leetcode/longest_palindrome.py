# https://leetcode.com/problems/longest-palindrome/submissions/
# abcceccdd
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # table to keep track of the occurances of letters
        table = {}
        
        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1
        
        # keep track of evens
        evens = 0
        # keep track of odds
        odds = 0
        single = 0
        
        for char in table:
            if table[char] % 2 == 0:
                evens += table[char]
            else:
                odds += (table[char] - 1)
                single = 1
            
        
        return evens + odds + single
                
        
