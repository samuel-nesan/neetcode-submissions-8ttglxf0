class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours > h:
                left = mid + 1
            else:
                k = mid
                right = mid - 1
        return k
        