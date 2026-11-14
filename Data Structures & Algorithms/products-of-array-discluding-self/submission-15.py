class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pairs = {}
        pairs_r = {}
        c = 1
        for i, n in enumerate(nums):
            pairs[i] = c
            c *= n
        c = 1
        for i in range(len(nums)-1, -1, -1):
            pairs_r[i] = c
            c *= nums[i]

        for i in range(len(pairs)):
            pairs[i] *= pairs_r[i]

        return (list(pairs.values()))