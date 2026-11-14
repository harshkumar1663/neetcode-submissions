class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        c = 1
        r = 1
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                c+=1
            else:
                c  = 1
            if c > r:
                r = c
        return (r)