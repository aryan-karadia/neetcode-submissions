class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        noDupes = set(nums)
        resArray = list(noDupes)
        resArray.sort()
        res = 1
        count = 1
        for i in range(1, len(resArray)):
            if resArray[i - 1] + 1 == resArray[i]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        
        return max(res, count)
