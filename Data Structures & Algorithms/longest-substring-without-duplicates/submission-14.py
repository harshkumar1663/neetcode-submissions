class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for ch in range(len(s)):
            while s[ch] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[ch])
            res = max(res, ch - l + 1)
        return res