class Solution:

    def encode(self, strs: List[str]) -> str:
        hash = {}
        s = ""
        for word in strs:
            s += str(len(word)) + "@" + word
        return s
    def decode(self, s: str) -> List[str]:
        r = []
        w = ""
        i = 0 
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '@':
                j += 1
            l = int(s[i:j])  
            word = s[j+1:j+1+l]
            r.append(word)
            i = j + 1 + l
        return r