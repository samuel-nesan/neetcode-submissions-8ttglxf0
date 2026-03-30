class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for s in strs:
            value = "".join(sorted(s))
            if value not in values:
                values[value] = [s]
            else:
                values[value].append(s)
        #res = []
        #for val in values:
        #    res.append(values[val])
        return list(values.values())