class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = sorted(list(set(nums)))
        print(n)
        l = 1
        c = 1
        for i in range(len(n)-1):
            if n[i]+1 == n[i+1]:
                c += 1
            elif c > l:
                l = c
                c = 1
            else : 
                c = 1
        return (c if l<c else l)