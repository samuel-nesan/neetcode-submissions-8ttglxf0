class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in values:
                return [values[value], i]
            values[num] = i
