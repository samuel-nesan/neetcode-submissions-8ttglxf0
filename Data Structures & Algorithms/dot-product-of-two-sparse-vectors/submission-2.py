class SparseVector:
    def __init__(self, nums: List[int]):
        self.val = []
        for i, num in enumerate(nums):
            if num != 0:
                self.val.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p, q = 0, 0
        res = 0

        while p < len(self.val) and q < len(vec.val):
            if self.val[p][0] == vec.val[q][0]:
                res += self.val[p][1] * vec.val[q][1]
                p += 1
                q += 1
            elif self.val[p][0] < vec.val[q][0]:
                p += 1
            else:
                q += 1
        return res 

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
