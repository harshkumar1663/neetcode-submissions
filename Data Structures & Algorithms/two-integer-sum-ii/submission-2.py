class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}

        for i,n in enumerate(numbers):
            c = target - n
            if c in s:
                return([s[c]+1,i+1])
                break
            s[n] = s.get(n,0) + i