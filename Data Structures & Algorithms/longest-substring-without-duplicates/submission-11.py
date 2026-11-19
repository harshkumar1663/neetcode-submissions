class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,f = 0,1
        w = s[0]
        nw = w
        while f < len(s):
            if s[f] not in w:
                w += s[f]
            else:
                if len(w) > len(nw):
                    nw = w
                idx = w.index(s[f])
                w = w[idx + 1:] + s[f]
            f += 1
        if len(w) > len(nw):
            nw = w
        return len(nw)