class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = []
        for i in nums:
            if i in s:
                return True
            else:
                s.append(i)
        return False