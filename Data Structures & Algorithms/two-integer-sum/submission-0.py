class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            value = target - num
            if num in values:
                return [values[num], i]
            values[value] = i
