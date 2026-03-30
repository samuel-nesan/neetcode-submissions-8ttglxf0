class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, num in enumerate(nums):
            val = target - num
            if num in values:
                return [values[num], i]
            else:
                values[val] = i