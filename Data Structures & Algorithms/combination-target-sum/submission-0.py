class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            total = 0
            for num in path:
                total += num
            if index == len(nums) or total >= target:
                if total == target:
                    res.append(path[:])
                return


            path.append(nums[index])
            backtrack(index, path)
            path.pop()

            backtrack(index + 1, path)
        
        backtrack(0, [])

        return res
                