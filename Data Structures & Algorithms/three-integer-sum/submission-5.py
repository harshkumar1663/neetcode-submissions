class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums)-1
            target = -n
            while left < right :
                sum = nums[left] + nums[right]
                if sum == target:
                    a = [nums[i], nums[left], nums[right]]
                    if a not in res : 
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                if sum < target: 
                    left += 1
                if sum > target:
                    right -= 1
        return res