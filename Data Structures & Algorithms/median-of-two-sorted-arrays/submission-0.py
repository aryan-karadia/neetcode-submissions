class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        l, r = 0, len(merged) - 1
        if len(merged) % 2 == 0:
            # even
            mid = (l + r) // 2
            val = (merged[mid] + merged[mid + 1]) / 2
        else:
            # odd
             mid = (l + r) // 2
             val = merged[mid]

        return val
