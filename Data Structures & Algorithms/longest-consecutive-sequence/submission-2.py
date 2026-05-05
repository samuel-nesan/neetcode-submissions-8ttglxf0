class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        res = 0

        for n in nums:
            count = 1
            if n - 1 in values: continue
            while n + 1 in values:
                n += 1
                count += 1
            res = max(count, res)
        return res
        