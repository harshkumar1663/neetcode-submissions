class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        mp = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                p = prices[right] - prices[left]
                mp = max(mp, p)
            else:
                left = right
            right += 1
        return mp