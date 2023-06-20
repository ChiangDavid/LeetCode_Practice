#Brute Force
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            res.append(count)
        
        return res
      
# Optimal solution
class Solution:
		def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      #We create a new sorted array
      #Because previous number will always smaller than current
			temp = sorted(nums)
			mapping = {}
			result = []
      #stored into dictionary
      #value:index
			for i in range(len(temp)):
				if temp[i] not in mapping:
					mapping[temp[i]] = i
          
			for i in range(len(nums)):
        #append the number's index to array and return
				result.append(mapping[nums[i]])
			return result
