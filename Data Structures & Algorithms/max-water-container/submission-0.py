class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        area = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l

            area = max(area, height * width)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return area