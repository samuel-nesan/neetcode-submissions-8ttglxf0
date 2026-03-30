class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                pivot = mid
                break
        
        left = 0
        right = len(nums) -1

        if pivot > 0 and target >= nums[pivot] and target >= nums[left]:
            right = pivot - 1
        else:
            left = pivot
        
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
