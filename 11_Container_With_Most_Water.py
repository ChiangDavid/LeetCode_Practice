class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            shortest = min(height[left], height[right])
            volume = shortest * (right - left)
            result = max(result, volume)
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
        
        return result
