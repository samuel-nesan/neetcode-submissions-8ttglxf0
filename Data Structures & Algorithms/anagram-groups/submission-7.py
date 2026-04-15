class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val = defaultdict(list)
        
        for s in strs:
            val[tuple(sorted(s))].append(s)
        return list(val.values())