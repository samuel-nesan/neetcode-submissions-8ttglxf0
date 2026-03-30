class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curSum = 0
        L = 0
        res = 0


        for R in range(len(arr)):
            curSum += arr[R]
            if R - L + 1 > k:
                curSum -= arr[L]
                L += 1
            if R - L + 1 == k and curSum >= target:
                res += 1
        return res

            