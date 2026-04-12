class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        window = set()

        while r < len(nums):
            if nums[r] not in window:
                window.add(nums[r])
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
