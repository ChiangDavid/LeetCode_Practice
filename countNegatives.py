# 1351. Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

# Brute Force:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #Brute force
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    count += 1
        return count
      
#Binary Search:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        count = 0
        for row in range(len(grid)):
            start, end = 0, cols-1
            while start <= end:
                mid = (start + end) //2
                if grid[row][mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            count += cols - start
        return count
