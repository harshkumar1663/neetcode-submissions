class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        f = [[] for i in range(len(nums)+1)]
        r = []
        for i in nums:
            count [i] = count.get(i, 0) + 1
        
        for n, c in count.items():
            f[c].append(n)
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                r.append(n)
                if len(r) == k:
                    return r