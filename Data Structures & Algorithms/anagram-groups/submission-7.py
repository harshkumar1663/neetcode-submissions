class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        clusters = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in clusters:
                clusters[key] = []
        
            clusters[key].append(word)
        return list(clusters.values())