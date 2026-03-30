class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0
        L = 0
        res = 0

        for R in range(len(arr)):
            if R - L + 1 > k:
                curSum -= arr[L]
                L += 1
            curSum += arr[R]
            if R - L + 1 == k and curSum/k >= threshold:
                res += 1
        return res

            