class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = {}
        r = {}
        p = 1
        for i in range (len(nums)):
            l[i] = (p)
            p = p*nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] = (p)
            p = p*nums[i]

        res = {}
        for i in range(len(l)):
            res[i] = (l[i] * r[i])
        return list(res.values())