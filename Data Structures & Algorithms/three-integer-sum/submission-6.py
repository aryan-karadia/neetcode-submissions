class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                current = a + nums[j] + nums[k]
                if current == 0:
                    result.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif current < 0:
                    j += 1
                else:
                    k -= 1
            
        return result
 

            
            
            
