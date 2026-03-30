class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            stone3 = stone1 - stone2

            if stone3 < 0:
                heapq.heappush(stones, stone3)
        
        return -stones[0] if len(stones) else 0
        