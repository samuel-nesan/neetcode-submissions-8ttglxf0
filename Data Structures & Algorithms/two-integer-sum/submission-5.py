class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in values:
                return [values[val], i]
            values[num] = i