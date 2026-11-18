class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil 
        left, right = 1, max(piles)
        res = right
        while left <= right:
            hours = 0
            k = (left + right)//2
            for p in piles:
                hours += ceil(p/k)
            if hours <= h:
                res = min(res,k)
                right = k-1
            else:
                left = k + 1
        return res