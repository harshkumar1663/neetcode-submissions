class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        r = []
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            c[i] = c.get(i,0) + 1
        
        for i, n in c.items():
            freq[n].append(i)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                r.append(n)
                if len(r) == k:
                    return r