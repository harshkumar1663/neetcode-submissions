class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        ht = {}

        for char in s : 
            hs[char] = hs.get(char, 0) + 1
        for char in t : 
            ht[char] = ht.get(char, 0) + 1
        
        if hs == ht:
            return True
        else : 
            return False