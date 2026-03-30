class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax, gMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            total += n
            curMax = max(curMax, 0)
            curMin = min(curMin, 0)
            curMax += n
            curMin += n
            gMax = max(gMax, curMax)
            gMin = min(gMin, curMin)


        return max(gMax, total-gMin) if gMax > 0 else gMax