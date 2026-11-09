class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hs = {}
        ht = {}


        for i in s:
            hs[i] = hs.get(i,0) + 1
        for i in t:
            ht[i] = ht.get(i,0) + 1
        
        for key in hs:
            if hs[key] != ht.get(key,0):
                return False
        return True