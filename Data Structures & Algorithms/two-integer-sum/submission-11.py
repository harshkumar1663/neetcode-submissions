class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in h:
                return [h[c],i]
            h[nums[i]] = h.get(nums[i],0) + i
