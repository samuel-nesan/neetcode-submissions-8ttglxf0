class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            else:
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target > row[mid]:
                        left = mid + 1
                    elif target < row[mid]:
                        right = mid - 1
                    else:
                        return True
        return False