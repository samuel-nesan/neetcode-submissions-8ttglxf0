class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        pivot = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid
            
        pivot = right
        left, right = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
