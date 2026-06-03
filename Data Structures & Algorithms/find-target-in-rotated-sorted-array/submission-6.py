class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                pivot = m
                r = m - 1

        l, r = 0, len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1