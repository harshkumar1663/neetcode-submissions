class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = []
        for i in s:
            if i.isalnum():
               d.append(i.lower())
        n = len(d)
        if n == 0 or n == 1 :
            return True
        c = 0
        for i in range(n):
            if i < (n/2):
                if d[i] == d[n-i-1]:
                    c = 1
                else:
                    return False

        if c == 1:
            return True
        else:
            return False