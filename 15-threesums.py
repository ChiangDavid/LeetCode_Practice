# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Notice that the solution set must not contain duplicate triplets.

#Mine solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            L, R = i + 1, len(nums)-1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    result.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif total > 0:
                    R -= 1
                elif total < 0:
                    L += 1

        return list(result)
      
      
#Other solutions
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                # to avoid duplicates
                continue
            L, R = i + 1, len(nums)-1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    # Skip all duplicates on left side
                    while L < R and nums[L - 1] == nums[L]:
                        L += 1
                    
                    # Skip all duplicates on right side
                    while L < R and nums[R + 1] == nums[R]:
                        R -= 1
                elif total > 0:
                    R -= 1
                elif total < 0:
                    L += 1

        return result
        
