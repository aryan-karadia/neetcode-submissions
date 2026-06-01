class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        n = len(nums)

        i = 0
        j = i + 1
        k = j + 1


        # outer loop for i
        while i + 2 < n:
            j = i + 1
            # inner loop for j
            while j < n:
                k = j + 1
                # inner inner loop for k
                while k < n:
                    val1 = nums[i]
                    val2 = nums[j]
                    val3 = nums[k]

                    if (val1 + val2 + val3) == 0:
                        valid = [val1, val2, val3]
                        valid.sort()
                        res.add(tuple(valid))
                    k += 1
                j += 1
            i += 1

        return list(res)
